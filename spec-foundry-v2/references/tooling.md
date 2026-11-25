# Ferramentas locais

Requisito: Python 3.10+. Nenhum pacote externo obrigatório (scripts usam só stdlib). `pytest` é necessário apenas para a camada `target_system` do harness de evals.

## Ordem de execução

```bash
python3 scripts/init_project.py --project <dir> --slug <slug> --release r001
python3 scripts/validate_package.py --project <dir> --report <dir>/validation.json
python3 scripts/check_traceability.py --project <dir>
python3 scripts/run_evals.py --project <dir>
python3 scripts/bundle_project.py --project <dir> --output <dir>/<slug>-<release>.zip
```

## `init_project.py`

Cria a árvore de `foundation/<release>/` (model, docs/specs, docs/adr, evals, contracts), copia templates e recusa pasta existente sem `--force`.

| Parâmetro | Default |
| --- | --- |
| `--project` | obrigatório |
| `--slug` | nome da pasta |
| `--release` | `r001` |
| `--force` | desligado |

## `validate_package.py`

Valida contratos locais: JSON parseável, campos obrigatórios do modelo, `out_of_scope` não vazio, todo `REQ` com `acceptance`, todo `EVAL` com alvo, `cases.json` igual à lista do modelo (quando houver), ausência de marcador de rascunho, manifest coerente.

| Parâmetro | Uso |
| --- | --- |
| `--project` | raiz do projeto |
| `--release` | default `r001` |
| `--report` | grava JSON de validação |
| `--strict` | trata aviso como erro |

Exit 1 em erro. Não valida mérito semântico nem executa testes.

## `check_traceability.py`

Lê `model/project-model.json` e `evals/cases.json`, varre `tests/test_*.py` por AST e verifica R1–R5. Gera `docs/traceability.md`.

| Parâmetro | Default |
| --- | --- |
| `--project` | obrigatório |
| `--release` | `r001` |
| `--tests` | `tests` |
| `--marker` | `req` |
| `--check` | não gera o `.md`, só verifica |

## `run_evals.py`

Executa os casos nas três camadas e grava `evals/reports/<run_id>.json`, `latest.json` e `latest.md`. Exit 1 se algum caso falhar.

| Parâmetro | Default |
| --- | --- |
| `--project` | obrigatório |
| `--release` | `r001` |
| `--layer` | todas |
| `--quiet` | desligado |

`target_system` roda `pytest` uma única vez com todos os node ids e lê o JUnit XML — rápido e sem efeito colateral. `contract` instancia o app e lê o OpenAPI; `static` lê arquivos.

## `bundle_project.py`

Gera ZIP com os arquivos do projeto, excluindo `.venv`, cache, `sources/` e relatórios antigos. Calcula SHA-256 e escreve `manifest.json` com a lista de artefatos. Recusa sobrescrever ZIP existente.

## `common.py`

Funções compartilhadas: resolução de caminhos, leitura de JSON com erro claro, geração de IDs, serialização canônica, verificação de placeholder. Importado pelos demais scripts; não é executável isolado.

## Limites

Os scripts verificam estrutura e execução, não qualidade semântica, não pertinência clínica/jurídica e não autenticidade de aprovação. A leitura humana continua sendo o filtro final — e é ela que a matriz de rastreabilidade tenta tornar barata.
