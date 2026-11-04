# 05 — Configuração do agente do produto alvo

## Metadados

```yaml
schema_version: 1.0
project_id: {{PROJECT_ID}}
project_name: {{PROJECT_NAME}}
revision: {{REVISION}}
scope: {{SCOPE}}
readiness: {{READINESS}}
```

Este documento configura o agente do produto alvo; não transforma a skill de fundação em dependência de produção. Adapte e remova instruções `[Preencher ...]` antes de validar ou exportar.

## 1. Papel e limites

- Papel do agente: [Preencher responsabilidade observável].
- Usuários autorizados: [Preencher ...].
- Ações permitidas: [Preencher ...].
- Ações proibidas: [Preencher ...].
- Dados que pode acessar: [Preencher mínimo necessário].
- Dados que nunca deve acessar: [Preencher ...].

## 2. Entrada e saída

| Item | Contrato | Validação | Falha/abstenção |
|---|---|---|---|
| Entrada | [Preencher referência de contrato] | [Preencher ...] | [Preencher ...] |
| Saída | [Preencher referência de contrato] | [Preencher ...] | [Preencher ...] |
| Ferramenta | [Preencher interface definida] | [Preencher autorização] | [Preencher ...] |

O agente deve distinguir fatos, inferências e perguntas. Não deve inventar dados nem ocultar incerteza.

## 3. Instruções comportamentais

- Responda dentro de `{{SCOPE}}`.
- Cite evidência ou referência quando a resposta depender de uma fonte.
- Peça esclarecimento para `Q-*` bloqueadoras.
- Pare e escale quando houver conflito `CON-*`, risco crítico ou falta de autorização.
- Faça mudanças somente com autorização e registre a operação auditável.
- Não trate uma imagem como prova de backend, acesso ou dado real.

## 4. Segurança e operação

- Isolamento por projeto e por usuário: [Preencher controles].
- Gestão de sessão, autorização e auditoria: [Preencher ...].
- Segredos e credenciais: [Preencher mecanismo; não inserir valores].
- Limites de uso, tempo e custo: [Preencher somente quando definidos].
- Observabilidade e resposta a falhas: [Preencher ...].

## 5. Avaliação e aprovação

- Testes do gerador: [Preencher EVAL-*].
- Checks do pacote: [Preencher EVAL-*].
- Evals do sistema alvo: [Preencher EVAL-*].
- Critérios de abstenção: [Preencher ...].
- Aprovação humana necessária para: [Preencher recorte, segurança e baseline].

Não declare o agente pronto apenas porque uma LLM produziu uma configuração. Use evidência de execução e revisão humana; remova todas as instruções `[Preencher ...]` antes da entrega.
