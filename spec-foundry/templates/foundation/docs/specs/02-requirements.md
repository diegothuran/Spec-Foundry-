# 02 — Requisitos

## Metadados

```yaml
schema_version: 1.0
project_id: {{PROJECT_ID}}
project_name: {{PROJECT_NAME}}
revision: {{REVISION}}
scope: {{SCOPE}}
readiness: {{READINESS}}
```

Adapte os registros, substitua instruções `[Preencher ...]` e remova-as antes de validar ou exportar. Não declare aceitação humana por inferência da IA.

## 1. Regra de identificação

Cada requisito usa `REQ-*`, referencia evidência quando aplicável e pode apontar para `CLM-*`, `DEC-*`, `TASK-*`, `RSK-*` e `EVAL-*`. O caminho recomendado é SRC-* -> EVD-* -> CLM-* -> REQ-*.

Todo requisito deve ter `status: proposed`, `accepted` ou `deferred` e `priority: critical`, `high` ou `normal`. Severidade é campo de risco/avaliação, não do requisito. `accepted` exige decisão humana registrada; `deferred` exige motivo e condição de retorno.

## 2. Catálogo de requisitos

| ID | Tipo | Enunciado verificável | Status | Prioridade | Fonte/claim | Critério de aceitação | EVAL |
|---|---|---|---|---|---|---|---|
| REQ-001 | funcional | [Preencher uma capacidade observável] | proposed | high | CLM-001 | [Preencher resultado observável] | EVAL-001 |
| REQ-002 | qualidade | [Preencher propriedade sem inventar limiar] | proposed | normal | EVD-001 | [Preencher verificação] | EVAL-002 |
| REQ-003 | segurança | [Preencher controle autorizado] | proposed | critical | [Preencher ...] | [Preencher evidência de controle] | EVAL-003 |
| REQ-004 | dados | [Preencher contrato ou regra de integridade] | deferred | normal | Q-001 | [Preencher condição de retorno] | EVAL-004 |

## 3. Forma de especificar

- Use sujeito, comportamento, condição e resultado; evite adjetivos sem teste.
- Separe requisito funcional, qualidade, segurança, dados, operação e governança.
- Não transforme uma preferência visual em requisito de backend.
- Não invente metas clínicas, fiscais, financeiras, de disponibilidade ou desempenho.
- Se a medição ainda não existir, descreva o método de observação e abra `Q-*`.
- Declare permissões, dados mínimos, retenção e falhas quando forem relevantes.

## 4. Dependências e conflitos

| REQ | Depende de | Conflita com | Risco | Decisão necessária |
|---|---|---|---|---|
| REQ-001 | [Preencher IDs] | CON-001 | RSK-001 | DEC-001 |
| REQ-002 | [Preencher IDs] | [Preencher ...] | [Preencher ...] | [Preencher ...] |

## 5. Critérios de aceite e prova

Para cada `REQ-*`, registre uma prova reproduzível, os dados necessários, o oráculo aplicável e o relatório esperado. O estado `passed` só pode ser usado após execução; antes disso use `not_run` ou `blocked` no EVAL correspondente.

## 6. Revisão

- Requisitos propostos a discutir: [Preencher IDs].
- Requisitos aceitos por pessoa responsável: [Preencher IDs, nome e data].
- Requisitos adiados e condição de retorno: [Preencher ...].
- Mudanças de recorte que exigem aprovação humana: [Preencher ...].
