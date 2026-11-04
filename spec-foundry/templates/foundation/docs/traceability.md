# Rastreabilidade

## Metadados

```yaml
schema_version: 1.0
project_id: {{PROJECT_ID}}
project_name: {{PROJECT_NAME}}
revision: {{REVISION}}
scope: {{SCOPE}}
readiness: {{READINESS}}
```

Adapte a matriz e remova instruções `[Preencher ...]` antes de validar ou exportar. Rastreabilidade demonstra relações; não transforma uma relação fraca em evidência forte.

## 1. Cadeia canônica

A cadeia primária é `SRC-* -> EVD-* -> CLM-* -> REQ-* -> DEC-*`, com derivados para `TASK-*`, `RSK-*` e `EVAL-*`. Uma linha pode começar ou terminar antes quando a etapa ainda não existe, mas a lacuna precisa ser explícita.

## 2. Matriz principal

| Source | Evidence | Claim | Requirement | Decision | Task | Risk | Eval | Estado |
|---|---|---|---|---|---|---|---|---|
| SRC-001 | EVD-001 | CLM-001 | REQ-001 | DEC-001 | TASK-001 | RSK-001 | EVAL-001 | [Preencher ...] |
| SRC-002 | EVD-002 | CLM-002 | REQ-002 | [Preencher ...] | TASK-002 | RSK-002 | EVAL-002 | [Preencher ...] |
| [Preencher ...] | [Preencher ...] | [Preencher ...] | REQ-003 | DEC-002 | TASK-003 | [Preencher ...] | EVAL-003 | [Preencher ...] |

## 3. Registro de origem

| ID | Tipo | Descrição | Localização | Confiança | Observação |
|---|---|---|---|---|---|
| SRC-001 | source | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher ...] |
| EVD-001 | evidence | [Preencher observação verificável] | SRC-001 | [Preencher ...] | [Preencher ...] |
| CLM-001 | claim | [Preencher afirmação derivada] | EVD-001 | [Preencher ...] | [Preencher ...] |

## 4. Registros derivados

| ID | Tipo | Texto/ação | Antecessores | Responsável | Estado |
|---|---|---|---|---|---|
| REQ-001 | requirement | [Preencher ...] | CLM-001 | [Preencher ...] | proposed |
| DEC-001 | decision | [Preencher ...] | REQ-001 | [Preencher ...] | [Preencher ...] |
| TASK-001 | task | [Preencher ...] | REQ-001 | [Preencher ...] | [Preencher ...] |
| RSK-001 | risk | [Preencher ...] | EVD-001 | [Preencher ...] | [Preencher ...] |
| EVAL-001 | eval | [Preencher ...] | REQ-001 | [Preencher ...] | not_run |

## 5. Perguntas e conflitos

| ID | Natureza | Afeta | Descrição | Resolução necessária | Estado |
|---|---|---|---|---|---|
| Q-001 | pergunta | REQ-002 | [Preencher ...] | [Preencher pessoa/fato] | aberta |
| CON-001 | conflito | DEC-001 | [Preencher ...] | [Preencher decisão humana] | aberto |

## 6. Controles de qualidade

- Toda afirmação relevante tem EVD-* ou está marcada como hipótese.
- Todo REQ-* tem critério observável, severidade `critical`, `high` ou `normal` e estado `proposed`, `accepted` ou `deferred`.
- Toda decisão escolhida aponta para seu contexto e aprovação humana.
- Toda tarefa tem definição de pronto e dependências.
- Todo risco possui resposta, responsável ou condição de aceitação.
- Todo EVAL-* distingue camada, status e oráculo.
- Lacunas não são escondidas por uma porcentagem de cobertura agregada.

## 7. Gate humano

- Lacunas a revisar: [Preencher ...].
- Recorte confirmado: [Preencher ...].
- Pessoa, data e decisão: [Preencher ...].
