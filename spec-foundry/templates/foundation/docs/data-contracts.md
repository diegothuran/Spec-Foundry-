# Contratos de dados

## Metadados

```yaml
schema_version: 1.0
project_id: {{PROJECT_ID}}
project_name: {{PROJECT_NAME}}
revision: {{REVISION}}
scope: {{SCOPE}}
readiness: {{READINESS}}
```

Adapte os contratos ao produto alvo e remova instruções `[Preencher ...]` antes de validar ou exportar. Um contrato só é aceito quando uma pessoa responsável confirmar seu significado e sua fronteira.

## 1. Catálogo de contratos

| ID | Nome | Direção | Produtor | Consumidor | Versão | Classificação | REQ |
|---|---|---|---|---|---|---|---|
| CTR-001 | [Preencher ...] | entrada | [Preencher ...] | [Preencher ...] | 1.0 | [Preencher ...] | REQ-001 |
| CTR-002 | [Preencher ...] | saída | [Preencher ...] | [Preencher ...] | 1.0 | [Preencher ...] | REQ-002 |

## 2. Estrutura do contrato

### CTR-001 — [Preencher nome]

```yaml
schema_version: 1.0
contract_id: CTR-001
project_id: {{PROJECT_ID}}
revision: {{REVISION}}
fields:
  - name: [Preencher nome]
    type: [Preencher tipo]
    required: [Preencher true ou false]
    nullable: [Preencher true ou false]
    constraints: [Preencher ...]
    semantics: [Preencher significado]
```

Fonte/claim: [Preencher SRC-*/EVD-*/CLM-*]. Validação: [Preencher regras]. Dados sintéticos permitidos: [Preencher ...].

## 3. Compatibilidade e evolução

- Compatibilidade de leitura: [Preencher ...].
- Compatibilidade de escrita: [Preencher ...].
- Política de versão e migração: [Preencher ...].
- Campos desconhecidos: [Preencher ...].
- Ausência, nulidade e valores vazios: [Preencher ...].
- Erros de validação e retorno ao chamador: [Preencher ...].

## 4. Segurança e isolamento

- Dados pessoais ou sensíveis: [Preencher classificação].
- Minimização e retenção: [Preencher ...].
- Isolamento por `project_id`: [Preencher regra de armazenamento e consulta].
- Segredos e credenciais: [Preencher mecanismo, nunca valores].
- Auditoria e redaction: [Preencher ...].

## 5. Provas

| Contrato | Fixture | Validação | EVAL | Estado |
|---|---|---|---|---|
| CTR-001 | [Preencher referência] | [Preencher comando/observação] | EVAL-001 | not_run |
| CTR-002 | [Preencher referência] | [Preencher ...] | EVAL-002 | not_run |

Não marque uma prova como `passed` sem execução e relatório. Registre perguntas `Q-*`, conflitos `CON-*` e DEC-* relacionados antes de congelar o contrato.
