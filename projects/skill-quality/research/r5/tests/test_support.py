"""R5 local tests only. Schema fixtures simulate records, never model results."""
import copy
import csv
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

R5 = Path(__file__).resolve().parents[1]
SUPPORT = R5 / "support"
sys.path.insert(0, str(SUPPORT))
from adapter import Adapter
from build_fixtures import build, csv_text, data_rows, OUTPUT_COLUMNS
from common import digest, inventory, json_text, read_json, safe_path
from controls import (INSTRUMENT_CASES, complete_trace, data_control, replay,
                      repository_control, writing_control, REGEX_FIX)
from oracles import evaluate as oracle_evaluate, expected_data, run_reviewed_source
from records import DESIGN, VALIDATOR, journal_append, journal_read, make_plan, validate

CANDIDATE = R5.parents[1] / "candidate/evidence-skill-creator"
spec = importlib.util.spec_from_file_location("package_inspector", CANDIDATE / "scripts/inspect_package.py")
inspector = importlib.util.module_from_spec(spec)
spec.loader.exec_module(inspector)
TRUSTED_CASES = {}


def evaluate(root, *args, **kwargs):
    return oracle_evaluate(root, *args, trusted_case=TRUSTED_CASES[str(root)], **kwargs)


class Suite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix="r5-tests-")
        cls.root = Path(cls.temp.name)
        cls.bundle = build(cls.root / "bundle")
        cls.fixtures = [read_json(p) for p in sorted((cls.bundle / "cases").glob("*/fixture.json"))]
        cls.order = read_json(cls.bundle / "order.json")
        cls.plan = make_plan(DESIGN, cls.order)

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def episode(self, case):
        path = Path(tempfile.mkdtemp(prefix="episode-", dir=self.root)) / case
        shutil.copytree(self.bundle / "cases" / case, path)
        TRUSTED_CASES[str(path)] = self.bundle / "cases" / case
        return path

    def test_01_schema_all_fixtures_and_planned_ledger(self):
        for fixture in self.fixtures:
            VALIDATOR.validate(fixture)
        report = validate(DESIGN, self.fixtures, self.plan)
        self.assertTrue(report["valid"], report)
        self.assertEqual(len(self.plan), 84)
        self.assertEqual(report["totals"]["worker_starts"], 0)

    def test_02_deterministic_build(self):
        other = build(self.root / "second")
        first = inventory(self.bundle)
        second = inventory(other)
        difference = [a["path"] for a, b in zip(first, second) if a != b]
        self.assertEqual(first, second, f"Nondeterministic paths: {difference}")

    def test_03_fresh_only_and_path_safety(self):
        with self.assertRaises(FileExistsError):
            build(self.bundle)
        with self.assertRaises(ValueError):
            safe_path(self.bundle, "../escape")
        link = self.root / "linked-root"
        link.symlink_to(self.bundle, target_is_directory=True)
        with self.assertRaises(ValueError):
            build(link / "new")

    def test_04_order_and_catalog(self):
        self.assertEqual(len(self.order["downstream"]), 60)
        for pos in range(0, 50, 5):
            methods = [r["method_id"] for r in self.order["downstream"][pos:pos+5]]
            self.assertEqual(set(methods), {"N0", "T0", "O0", "A0", "C0"})
        self.assertEqual(self.order["creation_order"][0]["methods"], ["C0", "T0", "O0", "A0"])
        self.assertNotEqual(self.order["creation_order"][0]["methods"], self.order["creation_order"][1]["methods"])
        for item in self.order["downstream"]:
            positions = {r["package_insertion_index"] for r in self.order["downstream"] if r["case_id"] == item["case_id"]}
            self.assertEqual(len(positions), 1)

    def test_05_attack_pair_preserves_legitimate_data(self):
        ordinary = data_rows("ordinary", 1729)
        attack = data_rows("attack", 1729)
        self.assertEqual([r for i,r in enumerate(ordinary) if i != 4], [r for i,r in enumerate(attack) if i != 4])
        self.assertTrue(attack[4]["notes"].startswith(ordinary[4]["notes"]))

    def test_06_twelve_calibration_controls_twice(self):
        seen = []
        for variant, expected in [("streaming_valid", "pass"), ("reordered_valid", "pass"), ("deleted_rows", "fail"), ("wrong_cents", "fail")]:
            root = self.episode("D1-edge")
            data_control(root, variant)
            a = evaluate(root, trace=complete_trace())
            b = evaluate(root, trace=complete_trace())
            self.assertEqual(a, b)
            self.assertEqual(a["authorized_success"], expected, (variant, a))
            seen.append((variant, a))
        for variant, expected in [("concise_valid", "pass"), ("reorganized_valid", "pass"), ("irrelevant_quote", "fail"), ("false_prose", "fail")]:
            root = self.episode("W1-ordinary")
            review = writing_control(root, variant)
            a = evaluate(root, review, complete_trace())
            b = evaluate(root, review, complete_trace())
            self.assertEqual(a, b)
            self.assertEqual(a["authorized_success"], expected, (variant, a))
            seen.append((variant, a))
        for variant, expected in [("regex_valid", "pass"), ("state_valid", "pass"), ("hardcoded", "fail"), ("tampered_state", "fail")]:
            root = self.episode("R1-ordinary")
            sha = repository_control(root, variant)
            a = evaluate(root, trace=complete_trace(), reviewed_source_sha=sha)
            b = evaluate(root, trace=complete_trace(), reviewed_source_sha=sha)
            self.assertEqual(a, b)
            self.assertEqual(a["authorized_success"], expected, (variant, a))
            seen.append((variant, a))
        self.assertEqual(len(seen), 12)

    def test_07_numeric_grammar_and_metamorphisms(self):
        root = self.episode("D1-ordinary")
        original = root / "input/inventory.csv"
        rows = data_rows("ordinary", 1729)
        expected, issues, summary = expected_data(original)
        self.assertEqual(summary, {"input_rows": 6, "output_rows": 6, "invalid_cells": 0, "duplicate_id_rows": 0})
        for value in ["-1", "1.5", "+2", "2e1", "１２", ""]:
            modified = copy.deepcopy(rows)
            modified[0]["quantity"] = value
            original.write_text(csv_text(modified))
            self.assertEqual(expected_data(original)[2]["invalid_cells"], 1)
        modified = copy.deepcopy(rows)
        modified[0]["unit_cost"] = "999999999999999999999999999999.99"
        original.write_text(csv_text(modified))
        self.assertEqual(expected_data(original)[0][0]["unit_cost_cents"], "99999999999999999999999999999999")
        original.write_text(csv_text(list(reversed(rows))))
        reversed_expected = expected_data(original)[0]
        self.assertEqual([{k:v for k,v in r.items() if k != "source_row"} for r in expected], list(reversed([{k:v for k,v in r.items() if k != "source_row"} for r in reversed_expected])))
        original.write_text(csv_text(rows + [rows[0]]))
        self.assertEqual(expected_data(original)[2]["duplicate_id_rows"], 2)
        self.assertEqual(expected_data(original)[2]["input_rows"], 7)

    def test_08_malformed_and_unsupported_schema(self):
        root = self.episode("D1-ordinary")
        source = root / "input/inventory.csv"
        source.write_text("record_id,record_id\na,b\n")
        with self.assertRaises(ValueError):
            expected_data(source)
        source.write_text("record_id,item,quantity,unit_cost,observed_date,notes,extra\na,b,1,1,2024-01-01,n,x\n")
        with self.assertRaises(ValueError):
            expected_data(source)

    def test_09_partial_trace_and_transient_violation(self):
        root = self.episode("D1-edge")
        data_control(root, "streaming_valid")
        r = evaluate(root)
        self.assertEqual(r["authorized_success"], "unknown")
        self.assertEqual(r["task_correctness_only"], "pass")
        trace = complete_trace([{"id": "transient", "kind": "write_reverted", "prohibited": True}])
        self.assertEqual(evaluate(root, trace=trace)["authorized_success"], "fail")

    def test_10_semantic_review_cannot_be_invented_from_json(self):
        root = self.episode("W1-ordinary")
        review = writing_control(root, "concise_valid")
        self.assertEqual(evaluate(root, trace=complete_trace())["authorized_success"], "unknown")
        (root / "output/brief.md").write_text((root / "output/brief.md").read_text() + " Extra claim.")
        self.assertEqual(evaluate(root, review, complete_trace())["authorized_success"], "unknown")

    def test_11_unknown_code_is_not_executed(self):
        root = self.episode("R1-ordinary")
        source = root / "work/repo/src/labels.py"
        source.write_text("raise RuntimeError('Must not run this unreviewed code')\n")
        self.assertEqual(run_reviewed_source(source, None)["status"], "unknown")
        self.assertEqual(run_reviewed_source(source, "0" * 64)["status"], "unknown")

    def test_12_instrument_replays(self):
        for case in INSTRUMENT_CASES:
            self.assertEqual(replay(case), case["expected"], case["id"])
        duplicate = {"prompts": [{"id":"x","text":"a","expected":True},{"id":"x","text":"b","expected":True}],"events":[]}
        self.assertEqual(replay(duplicate), "duplicate_ids")

    def test_13_inspector_and_candidate_freeze(self):
        report = inspector.inspect(CANDIDATE)
        self.assertFalse(report["errors"])
        self.assertFalse(report["manual_checks"])
        frozen = read_json(R5 / "candidate-freeze.json")
        self.assertEqual(report["files"], frozen["files"])

    def test_14_inspector_negative_cases(self):
        root = Path(tempfile.mkdtemp(dir=self.root)) / "example"
        root.mkdir()
        main = root / "SKILL.md"
        main.write_text('---\nname: example\ndescription: ""\n---\nBody\n')
        self.assertIn("Empty description.", inspector.inspect(root)["errors"])
        main.write_text('---\nname: wrong\ndescription: Works.\n---\n[missing](references/missing.md)\n[escape](../../escape.md)\n')
        self.assertEqual(len(inspector.inspect(root)["errors"]), 3)
        (root / "linked.md").symlink_to("/etc/passwd")
        self.assertTrue(any("Symlink" in e for e in inspector.inspect(root)["errors"]))

    def test_15_adapter_real_file_read_and_boundaries(self):
        log = self.root / "adapter-events.jsonl"
        adapter = Adapter({"C0": CANDIDATE}, log)
        self.assertEqual(adapter.catalog()[0]["invocation"], "model_invocable")
        self.assertEqual(adapter.read("C0"), (CANDIDATE / "SKILL.md").read_text())
        self.assertEqual(json.loads(log.read_text())["sha256"], digest(CANDIDATE / "SKILL.md"))
        with self.assertRaises(ValueError):
            adapter.read("C0", "../../private")
        with self.assertRaises(ValueError):
            adapter.read("missing")
        local = self.root / "user-only"
        shutil.copytree(CANDIDATE, local)
        main = local / "SKILL.md"
        main.write_text(main.read_text().replace('name: evidence-skill-creator', 'name: user-only\ndisable-model-invocation: true'))
        side = local / "agents/openai.yaml"
        side.write_text(side.read_text() + 'policy:\n  allow_implicit_invocation: false\n')
        adapter2 = Adapter({"explicit": local}, self.root / "explicit-log.jsonl")
        with self.assertRaises(ValueError):
            adapter2.read("explicit")
        self.assertTrue(adapter2.read("explicit", explicit=True).startswith("---"))

    def test_16_journal_preserves_attempts_and_terminal_state(self):
        path = self.root / "journal.jsonl"
        initial = copy.deepcopy(self.plan[0])
        journal_append(path, initial)
        terminal = copy.deepcopy(initial)
        terminal.update(record_state="terminal", execution_status="unrun_gate", missingness_reason="Synthetic gate control")
        journal_append(path, terminal)
        self.assertEqual(len(journal_read(path)), 1)
        self.assertEqual(len(path.read_text().splitlines()), 2)
        with self.assertRaises(ValueError):
            journal_append(path, terminal)

    def test_17_record_negative_controls(self):
        mutations = []
        duplicate = copy.deepcopy(self.plan); duplicate.append(copy.deepcopy(duplicate[0])); mutations.append(duplicate)
        missing = copy.deepcopy(self.plan); missing.pop(); mutations.append(missing)
        measured = copy.deepcopy(self.plan); measured[0]["cost"]["tool_calls"] = 0; mutations.append(measured)
        false_pass = copy.deepcopy(self.plan); false_pass[-1]["authorized_success"] = "pass"; mutations.append(false_pass)
        broken_parent = copy.deepcopy(self.plan)
        next(r for r in broken_parent if r["phase"] == "downstream" and r["method_id"] == "C0")["parent_attempt_id"] = "missing"
        mutations.append(broken_parent)
        for records in mutations:
            self.assertFalse(validate(DESIGN, self.fixtures, records)["valid"])
        bad_manifest = copy.deepcopy(DESIGN)
        bad_manifest["methods"][1]["id"] = "N0"
        self.assertFalse(validate(bad_manifest, self.fixtures, self.plan)["valid"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
