# Modelo de domínio

## Metadados

```yaml
schema_version: 1.0
project_id: {{PROJECT_ID}}
project_name: {{PROJECT_NAME}}
revision: {{REVISION}}
scope: {{SCOPE}}
readiness: {{READINESS}}
```

Adapte o modelo ao domínio descoberto e remova as instruções `[Preencher ...]` antes de validar ou exportar. Não trate nomes inferidos de uma imagem como entidades confirmadas.

## 1. Fronteira do domínio

- Propósito do modelo: [Preencher ...].
- Conceitos fora da fronteira: [Preencher ...].
- Linguagem ubíqua validada com pessoas do domínio: [Preencher ...].
- Claims que sustentam o modelo: [Preencher CLM-*].

## 2. Entidades e objetos de valor

| ID | Conceito | Tipo | Identidade | Atributos essenciais | Fonte/claim | REQ |
|---|---|---|---|---|---|---|
| ENT-001 | [Preencher ...] | entidade | [Preencher ...] | [Preencher ...] | CLM-001 | REQ-001 |
| ENT-002 | [Preencher ...] | objeto de valor | [Preencher ...] | [Preencher ...] | EVD-001 | REQ-002 |
| ENT-003 | [Preencher ...] | evento | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher ...] |

## 3. Relações e cardinalidade

| Relação | Origem | Destino | Cardinalidade | Regra | Evidência |
|---|---|---|---|---|---|
| REL-001 | ENT-001 | ENT-002 | [Preencher ...] | [Preencher ...] | EVD-001 |
| REL-002 | ENT-002 | ENT-003 | [Preencher ...] | [Preencher ...] | [Preencher ...] |

## 4. Estados e invariantes

| Conceito | Estado | Transição permitida | Pré-condição | Efeito | Erro/abstenção |
|---|---|---|---|---|---|
| ENT-001 | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher ...] |
| ENT-001 | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher ...] |

Invariantes essenciais: [Preencher regras que sempre devem permanecer verdadeiras].

## 5. Casos ambíguos

| ID | Ambiguidade | Interpretações | Impacto | Pergunta/conflito |
|---|---|---|---|---|
| Q-001 | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher ...] |
| CON-001 | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher decisão] |

## 6. Aprovação

- Alterações que exigem validação do domínio: [Preencher ...].
- Pessoa responsável e data: [Preencher ...].
- DEC-* que congelam vocabulário ou regra: [Preencher ...].
- Impacto em contratos, requisitos e evals: [Preencher ...].
