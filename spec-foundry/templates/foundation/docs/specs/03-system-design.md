# 03 — Desenho do sistema

## Metadados

```yaml
schema_version: 1.0
project_id: {{PROJECT_ID}}
project_name: {{PROJECT_NAME}}
revision: {{REVISION}}
scope: {{SCOPE}}
readiness: {{READINESS}}
```

Adapte este desenho ao produto alvo e remova instruções `[Preencher ...]` antes de validar ou exportar. Não escolha tecnologia por hábito.

## 1. Visão e fronteiras

- Responsabilidade do sistema: [Preencher ...].
- Fora da responsabilidade: [Preencher ...].
- Atores, sistemas externos e limites de confiança: [Preencher ...].
- Dados sensíveis e controles necessários: [Preencher apenas o que for evidenciado].

## 2. Componentes lógicos

| Componente | Responsabilidade | Entrada | Saída | Estado | REQ |
|---|---|---|---|---|---|
| CMP-001 | [Preencher ...] | [Preencher contrato] | [Preencher contrato] | [Preencher ...] | REQ-001 |
| CMP-002 | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher ...] | REQ-002 |

Descreva o fluxo nominal, fluxos de erro, reprocessamento, idempotência e abstenção. Se um componente ainda não estiver definido, mantenha a opção em aberto e abra `Q-*`.

## 3. Interfaces e dados

| Interface | Consumidor | Provedor | Contrato | Autorização | Falhas e observabilidade |
|---|---|---|---|---|---|
| IF-001 | [Preencher ...] | [Preencher ...] | [Preencher referência] | [Preencher ...] | [Preencher ...] |
| IF-002 | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher ...] |

## 4. Opções de solução

| Opção | Benefícios | Custos/riscos | Evidência | Estado |
|---|---|---|---|---|
| OPT-001 | [Preencher ...] | [Preencher ...] | [Preencher SRC/EVD] | em análise |
| OPT-002 | [Preencher ...] | [Preencher ...] | [Preencher ...] | em análise |

Não use Agno, Data Terminal, FastAPI, GCP, Heroku ou qualquer outra opção como default. Uma escolha somente entra como decisão em `DEC-*` após aprovação.

## 5. Segurança, operação e evolução

- Isolamento por projeto: [Preencher controles concretos].
- Credenciais e segredos: [Preencher mecanismo, sem valores reais].
- Logs, métricas, alertas e auditoria: [Preencher ...].
- Backup, recuperação e migração: [Preencher ...].
- Compatibilidade e versionamento: [Preencher ...].

## 6. Revisão de arquitetura

- DEC-* que precisam ser criados: [Preencher ...].
- CON-* ou Q-* que impedem fechamento: [Preencher ...].
- Impacto em REQ/TASK/RSK: [Preencher ...].
- Aprovação humana: [Preencher responsável, data e recorte aprovado].
