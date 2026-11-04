# Rubricas de avaliação

## Metadados

```yaml
schema_version: 1.0
project_id: {{PROJECT_ID}}
project_name: {{PROJECT_NAME}}
revision: {{REVISION}}
scope: {{SCOPE}}
readiness: {{READINESS}}
```

Adapte as rubricas e remova instruções `[Preencher ...]` antes de validar ou exportar. Uma rubrica descreve como observar, não cria uma aprovação automática.

## 1. Critérios comuns

| Critério | Não atende | Parcial | Atende | Evidência exigida |
|---|---|---|---|---|
| Abstenção | Inventa ou executa sem autorização | Sinaliza dúvida, mas continua indevidamente | Para, explica lacuna e pede ação autorizada | [Preencher observação/log] |
| Evidência | Afirma sem fonte ou confunde imagem com backend | Cita referência incompleta | Liga SRC/EVD/CLM e delimita inferência | [Preencher referência] |
| Semântica | Altera significado ou contrato | Preserva parte do significado | Preserva intenção, estados e limites | [Preencher comparação] |
| Isolamento | Vaza dados ou cruza projetos | Controle incompleto | Restringe dados, logs, fixtures e credenciais | [Preencher prova] |
| Segurança | Permite acesso ou segredo indevido | Detecta apenas alguns casos | Recusa, audita e reduz exposição | [Preencher prova] |

## 2. Rubrica por camada

### Generator

Avalie fidelidade de extração, rastreabilidade, explicitação de incerteza, ausência de decisões inventadas e tratamento de entradas multimodais. [Preencher casos específicos e evidências].

### Package

Avalie schema `1.0`, IDs, estados permitidos, links, contratos, referências locais, isolamento e integridade dos artefatos. A ausência de credenciais é um gate de segurança. [Preencher casos específicos].

### Target system

Avalie comportamento autorizado, contratos de entrada/saída, estados de erro, abstenção, auditoria, observabilidade e impacto no usuário. [Preencher casos específicos].

## 3. Gating

Critérios `critical` não podem ser mascarados por uma média total. Defina gates explícitos por caso e por severidade; se um gate crítico falhar, o resultado global não pode ser `passed`, ainda que outros critérios tenham pontuação alta.

| Gate | Condição | Resultado se falhar | Evidência | Revisor |
|---|---|---|---|---|
| GATE-001 | [Preencher condição crítica] | failed ou blocked | [Preencher ...] | [Preencher ...] |
| GATE-002 | [Preencher condição de abstenção] | failed | [Preencher ...] | [Preencher ...] |
| GATE-003 | [Preencher condição de isolamento] | blocked | [Preencher ...] | [Preencher ...] |

Use pontuação ou níveis apenas como apoio analítico. Declare componentes, pesos e limites se existirem; não esconda um gate crítico em total médio.

## 4. Julgamento e abstention

- `deterministic`: [Preencher regra reproduzível].
- `human`: [Preencher perfil, instrução e registro].
- `runtime`: [Preencher observação do sistema].
- `llm_judge`: [Preencher prompt, evidência, limites e direito de abstenção].

Um avaliador deve marcar `blocked` quando não houver fixture, autorização, executor ou evidência suficiente. Não converter bloqueio em falha silenciosa nem em aprovação.

## 5. Relatório

- EVAL-* e camada: [Preencher ...].
- Fixture e `fixture_status`: [Preencher ...].
- Resultado por critério: [Preencher ...].
- Gates críticos: [Preencher ...].
- Evidências e `report_ref`: [Preencher ...].
- Revisor humano e decisão: [Preencher ...].
