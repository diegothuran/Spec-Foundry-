#!/usr/bin/env python3
"""Cria scaffold incompleto. Não gera specs por LLM nem faz aprovação."""
import argparse
import json
import re
import shutil
from pathlib import Path
from common import CORE, SKILL_ROOT, dump


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--name', required=True)
    parser.add_argument('--project-id', required=True)
    parser.add_argument('--scope', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    if not re.fullmatch(r'[a-z0-9][a-z0-9-]*', args.project_id):
        parser.error('project-id precisa ser slug minúsculo')
    output = Path(args.output).expanduser().resolve()
    if output.exists():
        parser.error('Saída já existe; usar outra pasta/revisão, sem sobrescrever')
    if output.is_relative_to(SKILL_ROOT):
        parser.error('Dados de projetos não podem ficar dentro da skill')
    output.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SKILL_ROOT/'templates/foundation', output)
    for folder in ['model', 'schemas', 'sources', 'evals/fixtures', 'evals/reports', 'scripts']:
        (output/folder).mkdir(parents=True, exist_ok=True)
    values = {'PROJECT_NAME': args.name, 'PROJECT_ID': args.project_id, 'REVISION': 'r001', 'SCOPE': args.scope, 'READINESS': 'discovery'}
    for path in output.rglob('*.md'):
        content = path.read_text(encoding='utf-8')
        for key, value in values.items():
            content = content.replace('{{' + key + '}}', value)
        path.write_text(content, encoding='utf-8')
    model = json.loads((SKILL_ROOT/'templates/project-model.json').read_text(encoding='utf-8'))
    model.update({'project_name': args.name, 'project_id': args.project_id, 'scope': args.scope})
    shutil.copy2(SKILL_ROOT/'schemas/project-model.schema.json', output/'schemas/project-model.schema.json')
    for filename in ['common.py', 'validate_package.py', 'bundle_project.py']:
        shutil.copy2(SKILL_ROOT/'scripts'/filename, output/'scripts'/filename)
    paths = set(CORE) | {p.relative_to(output).as_posix() for p in output.rglob('*') if p.is_file()}
    model['artifacts'] = [{'path': name, 'requirement_refs': [], 'eval_refs': []} for name in sorted(paths)]
    dump(output/'model/project-model.json', model)
    dump(output/'evals/cases.json', [])
    print(f'Scaffold criado: {output}')
    print('Estado discovery. Requisitos/evidências ainda vazios e Markdown com instruções a preencher.')
    print('Validação/exportação vão falhar até completar o conteúdo. Não é fundação gerada/aprovada.')


if __name__ == '__main__':
    main()
