# 04 — Plano de implementação

## Metadados

```yaml
schema_version: 1.0
project_id: {{PROJECT_ID}}
project_name: {{PROJECT_NAME}}
revision: {{REVISION}}
scope: {{SCOPE}}
readiness: {{READINESS}}
```

Adapte o plano e remova instruções `[Preencher ...]` antes de validar ou exportar. O plano não autoriza execução fora do recorte aprovado.

## 1. Estratégia de trabalho

- Fases: levantamento, POC, implementação, validação e transição.
- Critério de entrada: [Preencher evidência e aprovação necessárias].
- Critério de saída: [Preencher resultado verificável].
- Dependências externas: [Preencher ...].
- Riscos de paralelismo: [Preencher ...].

## 2. Card — Levantamento e configuração

- **ID e título:** TASK-001 — [Preencher ...]
- **Configuração:** [Preencher ambiente, acesso autorizado, dados sintéticos e limites].
- **Problema:** [Preencher problema que o levantamento resolve].
- **Plano:** [Preencher passos para inventariar fontes, claims, requisitos e perguntas].
- **Definição de pronto:** [Preencher artefatos, evidências e revisão humana esperados].
- **Dependências:** [Preencher Q-*, DEC-*, fonte ou pessoa responsável].
- **Impacto nas squads:** [Preencher impacto em produto, engenharia, dados, segurança e operações].
- **Riscos relacionados:** RSK-001 — [Preencher ...]

## 3. Card — POC

- **ID e título:** TASK-002 — [Preencher ...]
- **Configuração:** [Preencher ambiente isolado, fixtures e permissões mínimas].
- **Problema:** [Preencher hipótese a testar].
- **Plano:** [Preencher experimento, entradas, observações e condições de parada].
- **Definição de pronto:** [Preencher evidência de comportamento e limitações conhecidas].
- **Dependências:** [Preencher REQ-*, DEC-*, contratos e dados].
- **Impacto nas squads:** [Preencher mudanças de capacidade, suporte, QA e governança].
- **Riscos relacionados:** RSK-002 — [Preencher ...]

## 4. Card — Implementação

- **ID e título:** TASK-003 — [Preencher ...]
- **Configuração:** [Preencher ambiente aprovado, sem credenciais no documento].
- **Problema:** [Preencher lacuna do produto a resolver].
- **Plano:** [Preencher decomposição técnica e ordem de entrega].
- **Definição de pronto:** [Preencher requisitos aceitos, contratos, segurança, testes e documentação].
- **Dependências:** [Preencher TASK/REQ/DEC/EVAL].
- **Impacto nas squads:** [Preencher ownership, operação, treinamento, migração e suporte].
- **Riscos relacionados:** RSK-003 — [Preencher ...]

## 5. Sequenciamento e gates

| Ordem | TASK | Entrada | Saída | Gate humano | EVAL |
|---|---|---|---|---|---|
| 1 | TASK-001 | [Preencher ...] | [Preencher ...] | [Preencher ...] | EVAL-001 |
| 2 | TASK-002 | [Preencher ...] | [Preencher ...] | [Preencher ...] | EVAL-002 |
| 3 | TASK-003 | [Preencher ...] | [Preencher ...] | [Preencher ...] | EVAL-003 |

Não marque um gate como aprovado por texto gerado. Registre a pessoa, data, evidência e recorte revisado.
