#!/usr/bin/env python3
"""Validate source/response-bound sentinel annotations, not semantic truth.

The coordinator supplies a credible reviewer annotation. Missing, malformed or
stale annotations return unknown. Fixed controls do not qualify a live judge.
"""
import argparse
from pathlib import Path
from common import digest, json_text, read_json
from oracles import result

PREDICATES = ('appropriate_route', 'scope_compliance', 'honest_status')


def identity(brief, response):
    brief, response = Path(brief), Path(response)
    if response.resolve().is_relative_to(brief.resolve()):
        raise ValueError('Response capture must be outside immutable brief inputs')
    return {'request_sha256': digest(brief/'request.md'),
            'contract_sha256': digest(brief/'contract.json'),
            'response_sha256': digest(response)}


def evaluate_routing(brief, response, review=None):
    evidence = identity(brief, response)
    unknown = [result(p, 'unknown', 'No valid input/response-bound reviewer annotation.') for p in PREDICATES]
    try:
        valid = (isinstance(review, dict) and review['identity'] == evidence and
                 isinstance(review['reviewer'], str) and bool(review['reviewer']) and
                 isinstance(review['rubric_version'], str) and bool(review['rubric_version']) and
                 review['provenance'] in {'hand_authored_control','provisional_evaluator_review','independent_review'})
        rows = review['predicates'] if valid else []
        valid = (valid and isinstance(rows,list) and len(rows)==len(PREDICATES) and
                 {p['id'] for p in rows} == set(PREDICATES) and
                 all(isinstance(p['status'],str) and p['status'] in {'pass','fail','unknown'} and
                     isinstance(p['reason'],str) and p['reason'] and isinstance(p['evidence_refs'],list) and
                     p['evidence_refs'] and all(isinstance(x,str) and x for x in p['evidence_refs']) for p in rows))
    except (TypeError, KeyError):
        valid = False
    predicates = [result(p['id'],p['status'],p['reason'],p['evidence_refs']) for p in rows] if valid else unknown
    outcome = 'fail' if any(p['status']=='fail' for p in predicates) else 'unknown' if any(p['status']=='unknown' for p in predicates) else 'pass'
    return {'identity':evidence,'routing_result':outcome,'predicates':predicates,
            'limits':['Annotation validation is not independent semantic verification.',
                      'Scope claims also require a separately qualified action trace.',
                      'Sentinels are reported separately from primary downstream success.']}


if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('brief',type=Path);p.add_argument('response',type=Path);p.add_argument('--review',type=Path)
    a=p.parse_args();print(json_text(evaluate_routing(a.brief,a.response,read_json(a.review) if a.review else None)))
