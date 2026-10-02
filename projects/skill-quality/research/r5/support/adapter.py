#!/usr/bin/env python3
"""Local catalog/read adapter, NOT a registered native skill tool or model runner.

Requires existing PyYAML. Catalog configuration explicitly maps IDs to local
package directories. All reads are allowlisted and logged with content hashes.
No package code is executed. Logs expose only sanitized package IDs/relative
paths, never private host prompts. Selection and budget supervision belong to R6.
"""
import argparse
import json
from pathlib import Path
import re
import yaml
from common import digest, json_text, read_json, safe_path, sha


class MetadataLoader(yaml.SafeLoader):
    """Small explicit profile: no aliases, merges or duplicate mapping keys."""
    def compose_node(self, parent, index):
        if self.check_event(yaml.AliasEvent):
            raise ValueError("YAML aliases are outside the metadata profile")
        return super().compose_node(parent, index)

    def construct_mapping(self, node, deep=False):
        result = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            if not isinstance(key, str) or key == "<<" or key in result:
                raise ValueError("Duplicate, merged or non-string YAML key")
            result[key] = self.construct_object(value_node, deep=deep)
        return result


def read_text(path):
    if not path.is_file() or path.stat().st_size > 2 * 1024 * 1024:
        raise ValueError("Missing or oversized resource")
    return path.read_bytes().decode("utf-8")


class Adapter:
    def __init__(self, packages, log):
        if not isinstance(packages, dict):
            raise ValueError("A file-reading catalog is required; generic model API alone is unsupported")
        self.packages = {key: Path(value).absolute() for key, value in packages.items()}
        self.log = Path(log)
        if any(not re.fullmatch(r"[a-zA-Z0-9_-]+", key) for key in self.packages):
            raise ValueError("Invalid catalog identifier")
        if any(not p.is_dir() or any(x.is_symlink() for x in (p, *p.parents)) for p in self.packages.values()):
            raise ValueError("Packages must be existing real directories")
        for root in self.packages.values():
            if self.log.resolve().is_relative_to(root.resolve()):
                raise ValueError("Event log must be outside immutable packages")
        if any(x.is_symlink() for x in (self.log, *self.log.parents)):
            raise ValueError("Log path may not contain symlinks")
        if self.log.exists() and not self.log.is_file():
            raise ValueError("Log must be a regular file")

    def metadata(self, id_):
        if id_ not in self.packages:
            raise ValueError("Package not in catalog")
        root = self.packages[id_]
        entry = safe_path(root, "SKILL.md")
        text = read_text(entry)
        if not text.startswith("---\n") or "\n---\n" not in text[4:]:
            raise ValueError("Missing frontmatter")
        front = yaml.load(text[4:].split("\n---\n", 1)[0], Loader=MetadataLoader)
        if not isinstance(front, dict) or not all(isinstance(front.get(k), str) and front[k].strip() for k in ("name", "description")):
            raise ValueError("Invalid name/description")
        user_only = front.get("disable-model-invocation", False)
        if type(user_only) is not bool:
            raise ValueError("Invocation flag must be boolean")
        sidecar = safe_path(root, "agents/openai.yaml")
        if sidecar.exists():
            metadata = yaml.load(read_text(sidecar), Loader=MetadataLoader)
            if not isinstance(metadata, dict) or not isinstance(metadata.get("policy", {}), dict):
                raise ValueError("Sidecar and policy must be mappings")
            policy = metadata.get("policy", {})
            implicit = policy.get("allow_implicit_invocation", True)
            if type(implicit) is not bool or implicit == user_only:
                raise ValueError("Inconsistent host invocation policy")
        return {"id": id_, "name": front["name"], "description": front["description"],
                "invocation": "explicit_user_only" if user_only else "model_invocable",
                "entrypoint_sha256": digest(entry)}

    def catalog(self):
        return [self.metadata(id_) for id_ in self.packages]

    def read(self, id_, relative="SKILL.md", explicit=False):
        if id_ not in self.packages:
            raise ValueError("Package not in catalog")
        meta = self.metadata(id_)
        if meta["invocation"] == "explicit_user_only" and not explicit:
            raise ValueError("User-only package needs explicit user invocation")
        path = safe_path(self.packages[id_], relative)
        content = read_text(path)
        data = content.encode("utf-8")
        event = {"kind": "load" if relative == "SKILL.md" else "resource_read", "target": id_,
                 "relative_path": relative, "sha256": sha(data), "bytes": len(data),
                 "mode": "explicit" if explicit else "file_read", "evidence_label": "adapter_read_observation"}
        with self.log.open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(event, sort_keys=True) + "\n")
        return content


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("catalog_config", type=Path, help="JSON mapping ID to approved package directory")
    parser.add_argument("--log", required=True, type=Path)
    parser.add_argument("--load")
    parser.add_argument("--resource", default="SKILL.md")
    parser.add_argument("--explicit", action="store_true")
    args = parser.parse_args()
    adapter = Adapter(read_json(args.catalog_config), args.log)
    print(adapter.read(args.load, args.resource, args.explicit) if args.load else json_text(adapter.catalog()))
