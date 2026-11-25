# Contrato do modelo — v2

`model/project-model.json` é o snapshot da verdade do projeto. Prosa e código derivam dele; quando divergem, o modelo ganha e o texto é corrigido.

## Metadados

```json
{
  "schema_version": "2.0",
  "project": {"name": "...", "slug": "...", "release": "r001", "status": "discovery|ready_for_review|approved_baseline"},
  "scope": {"in_scope": [...], "out_of_scope": [...]},
  "readiness": {"status": "...", "gates": [...]}
}
```

`out_of_scope` é obrigatório e não pode ser vazio. Um projeto sem fora de escopo não tem escopo — tem aspiração.

## Identificadores

| Prefixo | Entidade | Obrigatório em |
| --- | --- | --- |
| `SRC-*` | fonte (texto, PDF, imagem, URL, mensagem) | intake |
| `EVD-*` | evidência localizável (trecho + locator) | claim factual |
| `CLM-*` | afirmação (`user_definition`, `supported_inference`, `proposal`) | requisito |
| `REQ-*` | requisito testável | spec + eval + teste |
| `DEC-*` | decisão | ADR |
| `ASM-*` | assunção com impacto se falsa | modelo |
| `RSK-*` | risco com mitigação | modelo |
| `Q-*` | pergunta com dono e bloqueio | modelo |
| `CON-*` | conflito entre fontes | modelo |
| `TASK-*` | unidade de trabalho | plano |
| `EVAL-*` | caso de avaliação executável | `evals/cases.json` |
| `GATE-*` | critério de prontidão | `readiness` |

## Requisito (`REQ-*`)

Campos mínimos:

```json
{
  "id": "REQ-007",
  "title": "Conferência obrigatória antes da liberação",
  "layer": "domain|application|interface|integration|process",
  "priority": "P0|P1|P2",
  "statement": "Um resultado percorre ENTERED → REVIEWED → RELEASED...",
  "acceptance": ["liberar sem conferir falha", "fluxo completo conclui"],
  "spec": "docs/specs/03-review-and-report.md",
  "claim_refs": ["CLM-004"]
}
```

Regras:

- `statement` precisa de condição de sucesso **e** de erro. Sem condição de erro não é requisito, é desejo.
- `acceptance` tem no mínimo dois itens: um caminho feliz e um desvio.
- Todo `REQ` ativo precisa de ≥ 1 `EVAL` e ≥ 1 teste marcado. A ferramenta reprova.
- `layer` indica onde o requisito vive, não onde é testado.

## Assunção (`ASM-*`)

```json
{"id": "ASM-004", "statement": "...", "impact": "se falsa, ...", "validated_by": "REQ-008"}
```

Assunção é o oposto de evidência: existe justamente onde não há fonte. Declará-la é o que impede que ela vire alucinação. Toda assunção precisa de `impact` escrito em termos operacionais.

## Decisão (`DEC-*`) e ADR

Decisão material gera ADR em `docs/adr/NNNN-slug.md` com: Status, Contexto, Decisão, Alternativas, Consequências, Gatilhos de revisão. ADR sem alternativa descartada é justificativa retroativa, não decisão.

## Eval (`EVAL-*`)

```json
{
  "id": "EVAL-011",
  "req": "REQ-011",
  "layer": "target_system",
  "title": "...",
  "given": "...", "when": "...", "then": "...",
  "node_ids": ["tests/test_audit.py::test_trilha_de_auditoria_e_valida"]
}
```

- `layer: target_system` exige `node_ids` que existam de fato (verificados por AST, não por confiança).
- `layer: contract` exige `assertions` (ex.: `openapi_paths`, `openapi_version`, `schema_requires`).
- `layer: static` exige `assertions` de arquivo (`file_exists`, `file_contains`).

`execution_status` não é escrito à mão: vem do relatório gerado por `scripts/run_evals.py`. Status declarado sem relatório é removido pelo validador.

## Gate de prontidão (`GATE-*`)

| Gate | Critério objetivo |
| --- | --- |
| G1 Escopo | `out_of_scope` não vazio e coerente com `in_scope` |
| G2 Requisitos | todo `REQ` com `acceptance` ≥ 2 e condição de erro |
| G3 Evals | todo `EVAL` com camada executável e alvo existente |
| G4 Rastreabilidade | `check_traceability.py` sem violação |
| G5 Decisões | toda `DEC` material com ADR e alternativas |
| G6 Riscos | todo `RSK` com mitigação e status |

`ready_for_review` exige G1–G6. `approved_baseline` exige, além disso, aprovação humana registrada na mesma revisão (ver `review-and-approval.md`).

## Proibições

- Inventar `EVD` sem trecho localizável.
- Marcar `passed` sem relatório de execução real.
- Deixar `REQ` sem teste "porque o teste vem depois".
- Usar `TBD`, `TODO` ou `FIXME` em artefato normativo (o validador procura).
