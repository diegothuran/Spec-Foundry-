# Impacto de mudança

## Metadados

```yaml
schema_version: 1.0
project_id: {{PROJECT_ID}}
project_name: {{PROJECT_NAME}}
revision: {{REVISION}}
scope: {{SCOPE}}
readiness: {{READINESS}}
```

Adapte esta análise e remova instruções `[Preencher ...]` antes de validar ou exportar. Toda alteração relevante deve mostrar o que muda, o que permanece e quem aprova.

## 1. Registro da mudança

- ID da mudança: CHG-001 — [Preencher título].
- Solicitante e data: [Preencher ...].
- Motivo e evidência: [Preencher SRC-*/EVD-*/CLM-*].
- Estado atual e estado proposto: [Preencher ...].
- Recorte afetado: [Preencher ...].

## 2. Mapa de impacto

| Área | IDs afetados | Impacto | Compatibilidade | Ação necessária | Dono |
|---|---|---|---|---|---|
| Produto | [Preencher REQ-*] | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher ...] |
| Domínio | [Preencher ENT-*] | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher ...] |
| Dados | [Preencher CTR-*] | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher ...] |
| Sistema | [Preencher CMP/IF] | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher ...] |
| Agente | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher ...] |
| Evals | [Preencher EVAL-*] | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher ...] |
| Segurança | [Preencher RSK-*] | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher ...] |

## 3. Rastreabilidade alterada

| Relação anterior | Relação proposta | Evidência | DEC/ADR | Estado |
|---|---|---|---|---|
| [Preencher SRC->EVD->CLM->REQ] | [Preencher ...] | [Preencher ...] | [Preencher DEC-*] | proposta |
| [Preencher REQ->TASK->EVAL] | [Preencher ...] | [Preencher ...] | [Preencher ...] | proposta |

## 4. Plano de verificação

- Fixtures afetadas: [Preencher `missing`, `synthetic` ou `curated` e referências].
- Evals a reexecutar por camada: [Preencher generator/package/target_system].
- Contratos a validar: [Preencher ...].
- Critérios de abstenção, rollback ou bloqueio: [Preencher ...].
- Relatórios esperados: [Preencher ...].

Não diga que a mudança está segura antes da execução. Se uma prova não puder ser feita, registre `blocked` e explique o motivo.

## 5. Decisão e aprovação

- Riscos novos ou alterados: [Preencher RSK-*].
- Perguntas e conflitos abertos: [Preencher Q-*/CON-*].
- ADR necessário: [Preencher DEC-* ou referência].
- Impacto nas squads: [Preencher produto, engenharia, dados, QA, segurança, operações].
- Aprovador humano do recorte: [Preencher nome/função].
- Aprovação, data e limitações: [Preencher ...].

## 6. Condição de encerramento

A mudança somente pode ser encerrada quando a análise estiver ligada a evidências, os contratos e evals afetados tiverem sido revisados, os bloqueios estiverem explícitos e uma pessoa responsável tiver registrado a decisão. Uma LLM pode redigir este documento, mas não pode aprovar seu próprio impacto.
