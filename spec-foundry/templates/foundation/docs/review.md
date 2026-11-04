# Revisão humana

## Metadados

```yaml
schema_version: 1.0
project_id: {{PROJECT_ID}}
project_name: {{PROJECT_NAME}}
revision: {{REVISION}}
scope: {{SCOPE}}
readiness: {{READINESS}}
```

Adapte o roteiro e remova instruções `[Preencher ...]` antes de validar ou exportar. A revisão humana é obrigatória para recorte, baseline, segurança e decisões que o material não sustenta.

## 1. Escopo e intenção

- O problema e o resultado desejado estão claros? [Preencher observação].
- O que está incluído e excluído em `{{SCOPE}}`? [Preencher ...]
- Existem objetivos indevidos derivados apenas de imagem? [Preencher ...]
- Há mudanças de escopo que precisam de decisão? [Preencher ...]

## 2. Evidência e rastreabilidade

- SRC-* possuem origem e localização? [Preencher ...]
- EVD-* distinguem observação de interpretação? [Preencher ...]
- CLM-* estão sustentados e limitados? [Preencher ...]
- REQ-*, DEC-*, TASK-*, RSK-* e EVAL-* estão ligados? [Preencher ...]
- Q-* e CON-* permanecem visíveis? [Preencher ...]

## 3. Produto, sistema e dados

- Requisitos têm estado `proposed`, `accepted` ou `deferred` e severidade `critical`, `high` ou `normal`? [Preencher ...]
- Contratos, invariantes e compatibilidade foram revisados? [Preencher ...]
- Isolamento entre projetos e ausência de credenciais foram verificados? [Preencher ...]
- Tecnologias só foram escolhidas quando definidas e aprovadas? [Preencher ...]

## 4. Evals

- Generator, package e target_system estão separados? [Preencher ...]
- Cada eval tem status, fixture, expected, oracle, executor e report_ref? [Preencher ...]
- `passed` aparece apenas com execução e evidência? [Preencher ...]
- Gates críticos e critérios de abstenção estão explícitos? [Preencher ...]
- Não há thresholds clínicos, fiscais ou outros limites inventados? [Preencher ...]

## 5. Decisão da revisão

| Item | Resultado | Evidência | Ação |
|---|---|---|---|
| Recorte | [Preencher aprovado/ajustar] | [Preencher ...] | [Preencher ...] |
| Readiness | [Preencher discovery/ready_for_review/approved_baseline] | [Preencher ...] | [Preencher ...] |
| Segurança | [Preencher aprovado/bloqueado] | [Preencher ...] | [Preencher ...] |
| Baseline | [Preencher aprovado/adiado] | [Preencher ...] | [Preencher ...] |

- Revisor humano: [Preencher nome/função].
- Data: [Preencher ...].
- Decisão e limitações: [Preencher ...].
- Instruções `[Preencher ...]` removidas antes da entrega: [Preencher confirmação].

Uma LLM pode preparar a revisão, mas não pode se autoaprovar nem alterar o estado para `approved_baseline` sem decisão humana registrada.
