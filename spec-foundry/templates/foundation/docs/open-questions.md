# Perguntas abertas

## Metadados

```yaml
schema_version: 1.0
project_id: {{PROJECT_ID}}
project_name: {{PROJECT_NAME}}
revision: {{REVISION}}
scope: {{SCOPE}}
readiness: {{READINESS}}
```

Adapte as perguntas e remova instruções `[Preencher ...]` antes de validar ou exportar. Pergunta aberta não é falha do processo: é uma forma explícita de não inventar decisões.

## 1. Registro de perguntas

| ID | Pergunta | Motivo | Evidência relacionada | Afeta | Severidade | Responsável | Estado |
|---|---|---|---|---|---|---|---|
| Q-001 | [Preencher pergunta concreta] | [Preencher lacuna] | [Preencher SRC/EVD/CLM] | REQ-001 | high | [Preencher ...] | aberta |
| Q-002 | [Preencher ...] | [Preencher ...] | [Preencher ...] | DEC-001 | normal | [Preencher ...] | aberta |
| Q-003 | [Preencher ...] | [Preencher ...] | [Preencher ...] | TASK-001 | critical | [Preencher ...] | bloqueadora |

## 2. Como escrever uma pergunta útil

Uma boa pergunta identifica a decisão que está bloqueada, o contexto mínimo, a evidência já disponível e a resposta necessária. Evite perguntas genéricas como “está tudo certo?”.

Para cada item, registre se a resposta altera recorte, requisitos, modelo de dados, segurança, arquitetura, plano ou evals. Se a resposta for desconhecida, preserve o estado aberto e não substitua por uma escolha implícita.

## 3. Resolução

| ID | Resposta validada | Evidência nova | DEC/REQ afetado | Pessoa que confirmou | Data | Estado |
|---|---|---|---|---|---|---|
| Q-001 | [Preencher ...] | [Preencher EVD-*] | [Preencher IDs] | [Preencher ...] | [Preencher ...] | resolvida |
| Q-002 | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher ...] | adiada |

## 4. Perguntas sobre imagens e documentos

- O elemento visual é apenas referência de aparência ou representa comportamento obrigatório? [Preencher ...]
- Há texto, estado ou fluxo ausente na imagem que precisa de confirmação? [Preencher ...]
- O documento é fonte primária, rascunho ou material contextual? [Preencher ...]
- Existe autorização para usar os dados representados? [Preencher ...]

## 5. Gate de encerramento

- Perguntas bloqueadoras restantes: [Preencher IDs].
- Impacto aceito de perguntas adiadas: [Preencher ...].
- Aprovação humana do recorte: [Preencher pessoa, data e decisão].
- Instruções `[Preencher ...]` removidas antes da exportação: [Preencher confirmação].
