# Contrato de saída — v2

Árvore esperada de um projeto entregue. Nomes são contrato: as ferramentas procuram por eles.

```
<project>/
├── README.md                       # o que é, como rodar, o que não é
├── Makefile                        # install, test, evals, trace, contract, check
├── pyproject.toml                  # deps + config pytest (markers)
├── .github/workflows/ci.yml        # test + trace + contract + evals
├── src/<pkg>/                      # fundação executável
│   ├── domain/                     # regras puras, sem I/O
│   ├── application/                # casos de uso
│   ├── adapters/                   # persistência
│   ├── integrations/               # protocolos externos
│   └── api/                        # borda HTTP
├── tests/
│   ├── conftest.py                 # fixtures + helpers de fluxo
│   └── test_<área>.py              # @pytest.mark.req("REQ-00X")
├── tools/
│   ├── export_openapi.py
│   ├── run_evals.py
│   └── check_traceability.py
└── foundation/<release>/
    ├── manifest.json
    ├── model/project-model.json
    ├── docs/
    │   ├── specs/00-index.md, 01-...md, ...
    │   ├── adr/0001-....md
    │   ├── domain-model.md
    │   ├── data-contracts.md
    │   ├── assumptions-and-risks.md
    │   ├── open-questions.md
    │   └── traceability.md         # gerado
    ├── evals/
    │   ├── cases.json
    │   ├── rubrics.md
    │   └── reports/latest.json     # gerado
    └── contracts/openapi.json      # gerado
```

## Regras por artefato

| Artefato | Regra |
| --- | --- |
| `README.md` | abre com o que é; inclui estado medido (nº de testes, evals); inclui seção "o que não é" |
| `00-index.md` | tabela spec → requisitos + comandos de verificação |
| `specs/NN-*.md` | regras numeradas, tabela de erro, casos de borda, ganchos de eval |
| `adr/*.md` | Status, Contexto, Decisão, Alternativas, Consequências, Gatilhos |
| `cases.json` | lista de casos; cada um com `req`, `layer`, alvo executável |
| `manifest.json` | release, contagens reais, artefatos, evidência, fora de escopo |
| `contracts/openapi.json` | exportado do código, nunca escrito à mão |

## Nomenclatura de spec

`NN-<assunto>.md`, com `NN` de `00` a `99`. `00` é sempre o índice. Uma spec por área coesa, não uma por entidade: spec de uma entidade só vira dicionário de dados.

## Manifest mínimo

```json
{
  "release": "r001",
  "status": "ready_for_review",
  "requirements": 19,
  "cases": 26,
  "tests": 50,
  "artifacts": [{"path": "...", "kind": "spec|adr|evals|contract|model|evidence"}],
  "evidence": {"tests": 50, "test_command": "...", "evals_report": "evals/reports/latest.json"},
  "out_of_scope": ["..."]
}
```

Contagens precisam ser reais. Número inflado no manifest é a forma mais rápida de perder a confiança de quem lê.

## O que não vai no pacote

- Originais de cliente (`sources/` fica fora do ZIP por padrão).
- Cache, `.venv`, `__pycache__`, banco local.
- Relatório de execução inventado.
- Template preenchido com dado real de projeto anterior.
