#!/usr/bin/env python3
"""Materializa o schema da skill, sem chamadas externas ou LLM."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / 'spec-foundry'

def text(minimum=1):
    return {'type': 'string', 'minLength': minimum}

def nullable_text():
    return {'type': ['string', 'null'], 'minLength': 1}

def enum(*values):
    return {'type': 'string', 'enum': list(values)}

def arr(item, minimum=0):
    return {'type': 'array', 'items': item, 'minItems': minimum}

def refs():
    return dict(arr(text()), uniqueItems=True)

def obj(properties):
    return {'type': 'object', 'properties': properties, 'required': list(properties), 'additionalProperties': False}

def node(prefix, **properties):
    return obj({'id': {'type': 'string', 'pattern': '^' + prefix + '-[A-Za-z0-9][A-Za-z0-9_-]*$'}, **properties})

def ref(name):
    return {'$ref': '#/$defs/' + name}

locator = {
    'type': 'object',
    'properties': {
        'kind': enum('text_lines', 'pdf_page', 'image_region', 'user_message', 'web_section', 'mcp_record'),
        'ref': text(),
        'page': {'type': 'integer', 'minimum': 1},
        'lines': {'type': 'array', 'items': {'type': 'integer', 'minimum': 1}, 'minItems': 2, 'maxItems': 2},
        'bbox': {'type': 'array', 'items': {'type': 'number', 'minimum': 0, 'maximum': 1}, 'minItems': 4, 'maxItems': 4},
    },
    'required': ['kind', 'ref'], 'additionalProperties': False,
}
defs = {
    'source': node('SRC', kind=enum('text', 'user_message', 'pdf', 'image', 'web', 'mcp'), label=text(), ref=text(), local_path=nullable_text(), sha256={'type': ['string', 'null'], 'pattern': '^[a-f0-9]{64}$'}),
    'evidence': node('EVD', source_ref=text(), quote=nullable_text(), locator=locator, quality=enum('clear', 'uncertain')),
    'claim': node('CLM', text=text(), kind=enum('user_definition', 'supported_inference', 'proposal'), evidence_refs=refs()),
    'requirement': node('REQ', statement=text(), priority=enum('critical', 'high', 'normal'), status=enum('proposed', 'accepted', 'deferred'), claim_refs=refs(), decision_refs=refs()),
    'decision': node('DEC', statement=text(), rationale=text(), status=enum('proposed', 'approved', 'rejected'), revision=text(), scope=text(), requirement_refs=refs(), evidence_ref=nullable_text()),
    'task': node('TASK', title=text(), kind=enum('discovery', 'poc', 'implementation'), requirement_refs=refs(), dependency_refs=refs(), acceptance=text()),
    'risk': node('RSK', description=text(), severity=enum('critical', 'high', 'normal'), requirement_refs=refs(), mitigation=text()),
    'question': node('Q', text=text(), blocking={'type': 'boolean'}, status=enum('open', 'answered', 'deferred'), evidence_ref=nullable_text()),
    'conflict': node('CON', description=text(), claim_refs=refs(), blocking={'type': 'boolean'}, status=enum('open', 'resolved'), resolution_evidence_ref=nullable_text()),
    'eval_case': node('EVAL', layer=enum('generator', 'package', 'target_system'), requirement_refs=refs(), scenario=text(), input=text(), expected=text(), oracle=obj({'kind': enum('deterministic', 'human', 'runtime', 'llm_judge'), 'description': text()}), severity=enum('critical', 'high', 'normal'), fixture_status=enum('missing', 'synthetic', 'curated'), fixture_ref=nullable_text(), executor=nullable_text(), execution_status=enum('not_run', 'blocked', 'passed', 'failed'), report_ref=nullable_text()),
    'artifact': obj({'path': text(), 'requirement_refs': refs(), 'eval_refs': refs()}),
    'semantic_review': obj({'revision': text(), 'scope': text(), 'reviewer': text(), 'kind': enum('human', 'llm'), 'result': enum('pass', 'fail', 'needs_changes'), 'notes': text(), 'evidence_ref': nullable_text()}),
    'approval': obj({'revision': text(), 'scope': text(), 'actor': text(), 'decision': enum('approve', 'reject'), 'evidence_ref': text()}),
}
properties = {
    'schema_version': enum('1.0'),
    'project_id': {'type': 'string', 'pattern': '^[a-z0-9][a-z0-9-]*$'},
    'project_name': text(), 'revision': {'type': 'string', 'pattern': '^r[0-9]{3,}$'},
    'scope': text(), 'language': text(),
    'readiness': enum('discovery', 'ready_for_review', 'approved_baseline'),
}
for field, definition in [('sources', 'source'), ('evidence', 'evidence'), ('claims', 'claim'), ('requirements', 'requirement'), ('decisions', 'decision'), ('tasks', 'task'), ('risks', 'risk'), ('questions', 'question'), ('conflicts', 'conflict'), ('eval_cases', 'eval_case'), ('artifacts', 'artifact'), ('semantic_reviews', 'semantic_review'), ('approvals', 'approval')]:
    properties[field] = arr(ref(definition))
schema = obj(properties)
schema.update({'$schema': 'https://json-schema.org/draft/2020-12/schema', '$id': 'https://spec-foundry.example/skill/v1/project-model.schema.json', 'title': 'Spec Foundry Skill ProjectModel 1.0', '$defs': defs})
(ROOT/'schemas').mkdir(exist_ok=True)
(ROOT/'schemas/project-model.schema.json').write_text(json.dumps(schema, ensure_ascii=False, indent=2)+'\n')
model = {'schema_version': '1.0', 'project_id': 'project-id', 'project_name': '{{PROJECT_NAME}}', 'revision': 'r001', 'scope': '{{SCOPE}}', 'language': 'pt-BR', 'readiness': 'discovery'}
model.update({field: [] for field in properties if field not in model})
(ROOT/'templates/project-model.json').write_text(json.dumps(model, ensure_ascii=False, indent=2)+'\n')
print('Schema e template materializados.')
