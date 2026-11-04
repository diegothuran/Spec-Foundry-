# Especificação de avaliações

## Metadados

```yaml
schema_version: 1.0
project_id: {{PROJECT_ID}}
project_name: {{PROJECT_NAME}}
revision: {{REVISION}}
scope: {{SCOPE}}
readiness: {{READINESS}}
```

Adapte as avaliações e remova instruções `[Preencher ...]` antes de validar ou exportar. Não diga que algo passou sem execução, resultado verificável e relatório.

## 1. Camadas obrigatórias

As avaliações devem distinguir três objetos. `generator` testa se a transformação de texto/PDF/imagem produz artefatos estruturados sem inventar fatos. `package` verifica integridade, contratos, IDs, referências, isolamento e ausência de credenciais no pacote. `target_system` avalia o comportamento do produto alvo em seus fluxos autorizados.

Uma camada não substitui outra: um pacote íntegro não prova comportamento do target, e um target funcional não corrige um gerador que perdeu evidência.

## 2. Catálogo de evals

| ID | layer | Título | Requisito | Fixture | Status | Oracle |
|---|---|---|---|---|---|---|
| EVAL-001 | generator | [Preencher ...] | REQ-001 | [Preencher ...] | not_run | deterministic |
| EVAL-002 | package | [Preencher ...] | REQ-002 | [Preencher ...] | not_run | deterministic |
| EVAL-003 | target_system | [Preencher ...] | REQ-003 | [Preencher ...] | not_run | human |

## 3. Contrato de cada caso

```yaml
id: EVAL-001
project_id: {{PROJECT_ID}}
layer: generator
status: not_run
fixture_status: missing
fixture_ref: null
input_ref: [Preencher referência ou null]
expected: [Preencher resultado observável]
oracle:
  kind: deterministic
  description: [Preencher como decidir o resultado]
executor: null
report_ref: null
requirements:
  - REQ-001
```

Valores permitidos: `layer` é `generator`, `package` ou `target_system`; `status` é `not_run`, `blocked`, `passed` ou `failed`; `fixture_status` é `missing`, `synthetic` ou `curated`; `fixture_ref` aponta para fixture local ou é `null`. `oracle.kind` é `deterministic`, `human`, `runtime` ou `llm_judge`; `oracle.description` é obrigatório. `executor` e `report_ref` são `null` por padrão.

## 4. Conteúdo por camada

### Generator

Verifique preservação de fontes, evidências, claims, perguntas, conflitos, requisitos e decisões sem acrescentar escolhas não sustentadas. Inclua casos de entrada incompleta e imagem meramente visual. [Preencher ...]

### Package

Verifique schema, IDs, links relativos existentes, estados permitidos, contratos, isolamento por projeto, referências locais e ausência de credenciais. Inclua `model/project-model.json` e `evals/cases.json` somente como caminhos de integração definidos pelo projeto. [Preencher ...]

### Target system

Verifique fluxos do produto, autorização, abstenção, erros, contratos e observabilidade. Use fixtures autorizadas, sintéticas ou curadas; documente a origem. [Preencher ...]

## 5. Execução e bloqueios

- Comando ou executor: [Preencher ...].
- Ambiente isolado: [Preencher ...].
- Critério para `blocked`: [Preencher impedimento verificável].
- Relatório e artefatos: [Preencher ...].
- Reexecução e versionamento: [Preencher ...].

Não crie thresholds clínicos, fiscais, financeiros ou de desempenho sem fonte e aprovação. Quando a qualidade depender de julgamento, registre critérios e avaliador humano; quando usar `llm_judge`, documente limites, evidência e abstenção.

## 6. Gate humano

- Evals críticas que exigem revisão humana: [Preencher EVAL-*].
- Pessoa que aprova leitura do relatório: [Preencher ...].
- Data, escopo e decisão: [Preencher ...].
