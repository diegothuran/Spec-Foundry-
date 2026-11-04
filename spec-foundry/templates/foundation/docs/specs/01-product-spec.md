# 01 — Especificação do produto

## Metadados

```yaml
schema_version: 1.0
project_id: {{PROJECT_ID}}
project_name: {{PROJECT_NAME}}
revision: {{REVISION}}
scope: {{SCOPE}}
readiness: {{READINESS}}
```

Adapte o documento ao domínio real e remova as instruções `[Preencher ...]` antes de validar ou exportar. A primeira revisão deve ser `r001`.

## 1. Problema e resultado desejado

- Problema observado: [Preencher com o problema sustentado por SRC-*/EVD-*].
- Resultado desejado: [Preencher com mudança observável, sem prometer métrica não evidenciada].
- Usuários, operadores ou sistemas afetados: [Preencher ...].
- Não objetivos: [Preencher o que deliberadamente fica fora do recorte].

## 2. Escopo aprovado para levantamento

- Incluído: [Preencher ...].
- Excluído: [Preencher ...].
- Fronteiras e integrações: [Preencher somente integrações evidenciadas].
- Recorte atual: `{{SCOPE}}`.

## 3. Evidências e claims

| ID | Tipo | Conteúdo resumido | Fonte/referência | Confiança | Observação |
|---|---|---|---|---|---|
| SRC-001 | source | [Preencher ...] | [Preencher ...] | [Preencher ...] | [Preencher ...] |
| EVD-001 | evidence | [Preencher observação verificável] | SRC-001 | [Preencher ...] | [Preencher ...] |
| CLM-001 | claim | [Preencher afirmação derivada] | EVD-001 | [Preencher ...] | [Preencher ...] |

Não trate uma imagem como evidência de backend. Registre ambiguidade e abra `Q-*` quando uma interpretação depender de contexto ausente.

## 4. Cenários principais

### Cenário A — [Preencher nome]

- Ator e autorização: [Preencher ...]
- Pré-condições: [Preencher ...]
- Fluxo principal: [Preencher passos observáveis].
- Resultado esperado: [Preencher ...]
- Erros, limites e abstenção: [Preencher ...]
- REQ relacionados: [Preencher IDs REQ-*].

### Cenário B — [Preencher nome]

- Ator e autorização: [Preencher ...]
- Fluxo alternativo: [Preencher ...]
- Resultado esperado: [Preencher ...]
- REQ relacionados: [Preencher IDs REQ-*].

## 5. Critérios de aceitação

- Cada critério deve ser observável e ligado a um REQ-*.
- Critérios desconhecidos ficam como pergunta, não como comportamento presumido.
- Segurança, privacidade, isolamento e acessibilidade entram quando sustentados por evidência ou requisito.

## 6. Revisão humana

- Itens para aprovação de recorte: [Preencher ...].
- Itens para aprovação de readiness: [Preencher ...].
- Decisão humana e data: [Preencher ...].
