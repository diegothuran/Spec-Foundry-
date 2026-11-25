# Rastreabilidade e drift

## A cadeia

```
SRC/EVD → CLM → REQ → EVAL → teste (node id) → arquivo de código
```

Cada elo é verificável. A ferramenta `scripts/check_traceability.py` cobre os três últimos, que são os que apodrecem primeiro.

## Verificações (falham o comando)

| Regra | Verificação | Consequência |
| --- | --- | --- |
| R1 | todo `REQ` tem ≥ 1 caso de eval | requisito sem avaliação é intenção |
| R2 | todo `REQ` tem ≥ 1 teste marcado | requisito sem teste é prosa |
| R3 | todo `node_id` citado existe em `tests/` | eval quebrado é cobertura falsa |
| R4 | nenhum teste marca `REQ` inexistente | marcador órfão esconde requisito removido |
| R5 | todo caso aponta para `REQ` existente | caso órfão infla o número |

Saída: `docs/traceability.md` com a matriz REQ → casos → testes, mais a lista de testes sem caso vinculado. Teste órfão não é erro fatal, mas é sinal: ou o caso falta, ou o teste não pertence ao recorte.

## Por que AST e não grep

Ler decoradores por AST evita falso positivo de comentário, string ou decorador comentado. O script lê `tests/test_*.py`, encontra `FunctionDef` com prefixo `test_` e extrai `@pytest.mark.req("REQ-...")` do decorador real.

## Drift spec ↔ código

Rastreabilidade responde "existe teste?". Drift responde "o teste ainda mede o que o requisito diz?".

Sinais de drift:

- Spec descreve regra que nenhum teste menciona (mesmo com REQ coberto por outro teste).
- Teste passa, mas o nome do teste e o `statement` do requisito divergem de sentido.
- Contrato exportado muda e a spec de interface não muda.
- `acceptance` do requisito lista item que não tem asserção correspondente.

Rotina sugerida a cada release:

1. `check_traceability.py` (mecânico).
2. Leitura cruzada `statement` ↔ nome do teste ↔ asserção (humano, 10 minutos por spec).
3. Diff do contrato exportado (`git diff contracts/openapi.json`).
4. Se houver divergência: corrigir spec ou teste na mesma revisão. Nunca "depois".

## Quando a rastreabilidade quebra de propósito

Às vezes o requisito é retirado. O correto é:

1. Marcar `REQ` como `deferred` ou remover do recorte com decisão registrada.
2. Remover/ajustar casos e testes na mesma revisão.
3. Registrar o impacto no diff de revisão.

O que não se faz: deixar o teste passar apontando para requisito morto. Isso transforma a matriz em ficção auditável.
