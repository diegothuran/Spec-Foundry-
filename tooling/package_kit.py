#!/usr/bin/env python3
"""Empacota a skill no formato ZIP do Claude e o kit de manutenção em ZIP separado."""
import argparse
import hashlib
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {'__pycache__', '.pytest_cache', '.git', 'dist'}


def files(directory):
    selected = []
    for path in directory.rglob('*'):
        rel = path.relative_to(directory)
        if any(part in EXCLUDED for part in rel.parts):
            continue
        if path.is_symlink():
            raise ValueError('Symlink inesperado: ' + str(path))
        if path.is_file() and path.suffix not in ('.pyc', '.pyo'):
            selected.append(path)
    return sorted(selected)


def package(output, directory):
    with zipfile.ZipFile(output, 'x', zipfile.ZIP_DEFLATED) as z:
        for path in files(directory):
            if output.resolve() == path.resolve():
                raise ValueError('ZIP não pode incluir a si mesmo')
            z.write(path, directory.name + '/' + path.relative_to(directory).as_posix())
    with zipfile.ZipFile(output) as z:
        if z.testzip() is not None:
            raise ValueError('Falha de integridade de ZIP')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', required=True)
    args = parser.parse_args()
    output_dir = Path(args.output_dir).expanduser().resolve()
    if output_dir.is_relative_to(ROOT) and output_dir != ROOT/'dist':
        parser.error('Usar diretório externo ao kit ou a pasta dist excluída do arquivo')
    output_dir.mkdir(parents=True, exist_ok=True)
    upload = output_dir/'spec-foundry-claude.zip'
    kit = output_dir/'claude-spec-foundry-kit.zip'
    if upload.exists() or kit.exists():
        parser.error('ZIP de destino já existe; preservar a versão e usar outra pasta')
    manifest = []
    for path in files(ROOT):
        if path.name == 'MANIFEST-KIT.json':
            continue
        manifest.append({'path': path.relative_to(ROOT).as_posix(), 'bytes': path.stat().st_size, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
    (ROOT/'MANIFEST-KIT.json').write_text(json.dumps({'version': '1.0.0', 'purpose': 'claude_skill_source_kit', 'files': manifest, 'limitations': 'Hashes de conteúdo, não aprovação/autenticidade; comportamento Claude não avaliado por empacotamento.'}, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    try:
        package(upload, ROOT/'spec-foundry')
        package(kit, ROOT)
    except Exception:
        upload.unlink(missing_ok=True)
        kit.unlink(missing_ok=True)
        raise
    print('Upload Claude:', upload)
    print('Kit completo:', kit)
    print('O ZIP de upload possui somente a pasta-raiz spec-foundry; nenhuma instalação foi realizada.')


if __name__ == '__main__':
    main()
