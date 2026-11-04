# Premissas e riscos

## Metadados

```yaml
schema_version: 1.0
project_id: {{PROJECT_ID}}
project_name: {{PROJECT_NAME}}
revision: {{REVISION}}
scope: {{SCOPE}}
readiness: {{READINESS}}
```

Adapte o registro e remova instruções `[Preencher ...]` antes de validar ou exportar. Premissa não é fato; risco não deve ser reduzido por linguagem otimista sem evidência.

## 1. Premissas

| ID | Premissa | Base | Confiança | O que a invalida | Verificação | Estado |
|---|---|---|---|---|---|---|
| ASM-001 | [Preencher ...] | [Preencher SRC/EVD/CLM] | [Preencher ...] | [Preencher ...] | [Preencher ...] | aberta |
| ASM-002 | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher ...] | aberta |

Uma premissa deve ser convertida em requisito, pergunta, decisão ou risco quando seu impacto for relevante. Não trate uma escolha técnica como premissa estável sem aprovação.

## 2. Riscos

| ID | Risco | Causa | Consequência | Probabilidade | Impacto | Severidade | Dono | Estado |
|---|---|---|---|---|---|---|---|---|
| RSK-001 | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher ...] | critical | [Preencher ...] | aberto |
| RSK-002 | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher ...] | high | [Preencher ...] | aberto |
| RSK-003 | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher ...] | normal | [Preencher ...] | aberto |

## 3. Respostas e gatilhos

| Risco | Resposta preventiva | Plano de contingência | Gatilho | Dependências | EVAL |
|---|---|---|---|---|---|
| RSK-001 | [Preencher ...] | [Preencher ...] | [Preencher observação] | [Preencher ...] | EVAL-001 |
| RSK-002 | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher ...] | EVAL-002 |

Não invente thresholds clínicos, fiscais, financeiros ou operacionais. Quando um limite for necessário, abra `Q-*` e defina o método de aprovação e medição.

## 4. Revisão de segurança e isolamento

- Projetos separados por: [Preencher ...].
- Credenciais ausentes dos artefatos: [Preencher confirmação].
- Dados sintéticos ou autorizados: [Preencher ...].
- Riscos de inferência a partir de imagens: [Preencher ...].
- Riscos de autoaprovação por LLM: [Preencher controles].

## 5. Aceite humano

- Riscos críticos não aceitos automaticamente: [Preencher IDs].
- Aceites, responsáveis e datas: [Preencher ...].
- Premissas que ainda bloqueiam readiness: [Preencher ...].
