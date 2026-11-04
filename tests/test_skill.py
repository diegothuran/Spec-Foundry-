#!/usr/bin/env python3
"""Testes sintéticos de código local; não são evals do comportamento do Claude."""
import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1] / 'spec-foundry'
sys.path.insert(0, str(SKILL/'scripts'))
from common import CORE, digest, dump, load, validate


def fixture(root):
    root.mkdir()
    (root/'sources').mkdir()
    origin = root/'sources/input.txt'
    statement = 'O usuário deve visualizar somente os documentos do próprio projeto.'
    origin.write_text(statement + '\nRetenção ainda não definida.\n', encoding='utf-8')
    model = load(SKILL/'templates/project-model.json')
    model.update({'project_id': 'portal-demo', 'project_name': 'Portal sintético', 'scope': 'Visualização privada de documentos', 'revision': 'r001'})
    model['sources'] = [{'id': 'SRC-001', 'kind': 'text', 'label': 'Input sintético', 'ref': 'input.txt', 'local_path': 'sources/input.txt', 'sha256': digest(origin)}]
    model['evidence'] = [{'id': 'EVD-001', 'source_ref': 'SRC-001', 'quote': statement, 'locator': {'kind': 'text_lines', 'ref': 'sources/input.txt', 'lines': [1, 1]}, 'quality': 'clear'}]
    model['claims'] = [{'id': 'CLM-001', 'text': statement, 'kind': 'user_definition', 'evidence_refs': ['EVD-001']}]
    model['requirements'] = [{'id': 'REQ-001', 'statement': statement, 'priority': 'critical', 'status': 'proposed', 'claim_refs': ['CLM-001'], 'decision_refs': []}]
    model['tasks'] = [{'id': 'TASK-001', 'title': 'Testar isolamento', 'kind': 'poc', 'requirement_refs': ['REQ-001'], 'dependency_refs': [], 'acceptance': 'Acesso cruzado deve ser negado em teste sintético.'}]
    model['questions'] = [{'id': 'Q-001', 'text': 'Qual a retenção?', 'blocking': True, 'status': 'open', 'evidence_ref': None}]
    model['eval_cases'] = [{'id': 'EVAL-001', 'layer': 'target_system', 'requirement_refs': ['REQ-001'], 'scenario': 'Usuário tenta acessar documento de outro projeto.', 'input': 'Duas identidades e dois projetos sintéticos; preparar executor futuro.', 'expected': 'Negar acesso cruzado sem retornar conteúdo.', 'oracle': {'kind': 'runtime', 'description': 'Assert de autorização e ausência de dados cruzados em ambiente implementado.'}, 'severity': 'critical', 'fixture_status': 'missing', 'fixture_ref': None, 'executor': None, 'execution_status': 'not_run', 'report_ref': None}]
    model['artifacts'] = [{'path': name, 'requirement_refs': ['REQ-001'] if name == 'docs/specs/02-requirements.md' else [], 'eval_refs': []} for name in CORE]
    for name in CORE:
        path = root/name
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.suffix == '.md':
            path.write_text('# Documento sintético para teste estrutural\n\nNão é saída de um Claude nem gold semântico.\n\nREQ-001: ' + statement + '\n', encoding='utf-8')
    dump(root/'schemas/project-model.schema.json', load(SKILL/'schemas/project-model.schema.json'))
    save(root, model)
    return model


def save(root, model):
    dump(root/'model/project-model.json', model)
    dump(root/'evals/cases.json', model['eval_cases'])


class ContractTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)/'project'
        self.model = fixture(self.root)

    def tearDown(self):
        self.temp.cleanup()

    def result(self, exported=False):
        save(self.root, self.model)
        return validate(self.root, exported=exported)

    def assertFails(self):
        result = self.result()
        self.assertEqual(result['structural_status'], 'fail', result)

    def test_valid_discovery_is_not_approval(self):
        result = self.result()
        self.assertEqual(result['structural_status'], 'pass', result)
        self.assertEqual(result['declared_readiness'], 'discovery')
        self.assertEqual(self.model['eval_cases'][0]['execution_status'], 'not_run')

    def test_duplicate_id(self):
        self.model['claims'].append(copy.deepcopy(self.model['claims'][0]))
        self.assertFails()

    def test_reference_missing(self):
        self.model['requirements'][0]['claim_refs'] = ['CLM-missing']
        self.assertFails()

    def test_quote_invented(self):
        self.model['evidence'][0]['quote'] = 'Citação que não existe'
        self.assertFails()

    def test_hash_wrong(self):
        self.model['sources'][0]['sha256'] = '0'*64
        self.assertFails()

    def test_source_path_traversal(self):
        self.model['sources'][0]['local_path'] = '../outside.txt'
        self.assertFails()

    def test_artifact_path_traversal(self):
        self.model['artifacts'].append({'path': '../secret.txt', 'requirement_refs': [], 'eval_refs': []})
        self.assertFails()

    def test_secret_export(self):
        (self.root/'.env').write_text('FAKE=not-a-real-secret\n')
        self.model['artifacts'].append({'path': '.env', 'requirement_refs': [], 'eval_refs': []})
        self.assertFails()

    def test_symlink(self):
        (self.root/'alias.txt').symlink_to(self.root/'sources/input.txt')
        self.model['artifacts'].append({'path': 'alias.txt', 'requirement_refs': [], 'eval_refs': []})
        self.assertFails()

    def test_accepted_without_human_decision(self):
        self.model['requirements'][0]['status'] = 'accepted'
        self.assertFails()

    def test_ready_with_question(self):
        self.model['readiness'] = 'ready_for_review'
        self.assertFails()

    def test_deferred_blocking_question_still_blocks(self):
        self.model['questions'][0]['status'] = 'deferred'
        self.model['readiness'] = 'ready_for_review'
        self.assertFails()

    def test_uncertain_evidence_blocks_ready(self):
        self.model['questions'] = []
        self.model['evidence'][0]['quality'] = 'uncertain'
        self.model['readiness'] = 'ready_for_review'
        self.assertFails()

    def test_approval_not_inferred_from_pass(self):
        self.model['questions'] = []
        self.model['readiness'] = 'approved_baseline'
        self.assertFails()

    def declared_human_baseline(self):
        message = 'MENSAGEM SINTÉTICA DE TESTE: revisei r001 no recorte informado e aprovo a especificação de isolamento; os testes do alvo continuam não executados.'
        origin = self.root/'sources/approval.txt'
        origin.write_text(message + '\n', encoding='utf-8')
        self.model['sources'].append({'id': 'SRC-002', 'kind': 'user_message', 'label': 'Resposta humana simulada para testar código', 'ref': 'synthetic-message-002', 'local_path': 'sources/approval.txt', 'sha256': digest(origin)})
        self.model['evidence'].append({'id': 'EVD-002', 'source_ref': 'SRC-002', 'quote': message, 'locator': {'kind': 'user_message', 'ref': 'synthetic-message-002'}, 'quality': 'clear'})
        self.model['questions'] = []
        self.model['decisions'] = [{'id': 'DEC-001', 'statement': 'Aceitar requisito de isolamento no recorte', 'rationale': 'Confirmação explícita simulada, não aprovação real de produto.', 'status': 'approved', 'revision': 'r001', 'scope': self.model['scope'], 'requirement_refs': ['REQ-001'], 'evidence_ref': 'EVD-002'}]
        self.model['requirements'][0].update({'status': 'accepted', 'decision_refs': ['DEC-001']})
        self.model['semantic_reviews'] = [{'revision': 'r001', 'scope': self.model['scope'], 'reviewer': 'Revisor simulado', 'kind': 'human', 'result': 'pass', 'notes': 'Fixture somente para verificar contrato local.', 'evidence_ref': 'EVD-002'}]
        self.model['approvals'] = [{'revision': 'r001', 'scope': self.model['scope'], 'actor': 'Pessoa simulada', 'decision': 'approve', 'evidence_ref': 'EVD-002'}]
        self.model['readiness'] = 'approved_baseline'

    def test_human_records_allow_declared_baseline_not_runtime_pass(self):
        self.declared_human_baseline()
        result = self.result()
        self.assertEqual(result['structural_status'], 'pass', result)
        self.assertEqual(self.model['eval_cases'][0]['execution_status'], 'not_run')
        self.assertTrue(any('identidade humana' in note for note in result['limitations']))

    def test_newer_rejection_blocks_declared_baseline(self):
        self.declared_human_baseline()
        self.model['approvals'].append({**self.model['approvals'][0], 'decision': 'reject'})
        self.assertFails()

    def test_prior_revision_approval_invalid(self):
        self.model['questions'] = []
        self.model['readiness'] = 'approved_baseline'
        self.model['approvals'] = [{'revision': 'r000', 'scope': self.model['scope'], 'actor': 'Pessoa sintética', 'decision': 'approve', 'evidence_ref': 'EVD-001'}]
        self.assertFails()

    def test_target_eval_coverage(self):
        self.model['eval_cases'][0]['layer'] = 'package'
        self.assertFails()

    def test_critical_requirement_needs_critical_eval(self):
        self.model['eval_cases'][0]['severity'] = 'normal'
        self.assertFails()

    def test_pass_cannot_be_invented(self):
        self.model['eval_cases'][0]['execution_status'] = 'passed'
        self.assertFails()

    def test_local_report_cannot_be_target_report(self):
        path = self.root/'evals/reports/local.json'
        path.parent.mkdir(exist_ok=True)
        dump(path, {'scope': 'local_contract_checks', 'layer': 'package', 'revision': 'r001', 'case_ids': ['EVAL-001'], 'status': 'passed', 'executor': 'local', 'evidence_refs': ['sources/input.txt'], 'limitations': ['sintético']})
        self.model['eval_cases'][0].update({'execution_status': 'passed', 'executor': 'local', 'report_ref': 'evals/reports/local.json'})
        self.assertFails()

    def test_missing_fixture_not_real_path(self):
        self.model['eval_cases'][0]['fixture_ref'] = 'evals/fixtures/not-created.json'
        self.assertFails()

    def test_task_cycle(self):
        self.model['tasks'][0]['dependency_refs'] = ['TASK-001']
        self.assertFails()

    def test_eval_file_drift(self):
        dump(self.root/'evals/cases.json', [])
        result = validate(self.root)
        self.assertEqual(result['structural_status'], 'fail')

    def test_unresolved_template(self):
        (self.root/'README.md').write_text('# {{PROJECT_NAME}}\n')
        self.assertFails()

    def test_bbox_order(self):
        self.model['evidence'][0]['locator'] = {'kind': 'image_region', 'ref': 'image', 'bbox': [0.8, 0.1, 0.2, 0.9]}
        self.assertFails()

    def test_empty_scaffold_is_not_completed(self):
        target = Path(self.temp.name)/'new'
        command = [sys.executable, str(SKILL/'scripts/init_project.py'), '--name', 'Demo', '--project-id', 'demo', '--scope', 'POC', '--output', str(target)]
        completed = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(validate(target)['structural_status'], 'fail')
        repeated = subprocess.run(command, capture_output=True, text=True)
        self.assertNotEqual(repeated.returncode, 0)

    def test_export_excludes_sources_and_checks_manifest(self):
        save(self.root, self.model)
        output = Path(self.temp.name)/'bundle.zip'
        completed = subprocess.run([sys.executable, str(SKILL/'scripts/bundle_project.py'), '--project', str(self.root), '--output', str(output)], capture_output=True, text=True)
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        import zipfile
        extracted = Path(self.temp.name)/'extracted'
        with zipfile.ZipFile(output) as z:
            self.assertFalse(any('/sources/' in name for name in z.namelist()))
            z.extractall(extracted)
        exported_root = next(extracted.iterdir())
        result = validate(exported_root, exported=True)
        self.assertEqual(result['structural_status'], 'pass', result)
        self.assertTrue(any('original privado' in w for w in result['warnings']))
        self.assertEqual(validate(exported_root)['structural_status'], 'fail')
        (exported_root/'README.md').write_text('# arquivo alterado\n')
        self.assertEqual(validate(exported_root, exported=True)['structural_status'], 'fail')


if __name__ == '__main__':
    unittest.main(verbosity=2)
