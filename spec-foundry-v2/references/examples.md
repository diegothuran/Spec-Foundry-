# Exemplos de calibração

Todos os exemplos são sintéticos e não contêm dado de cliente.

## Exemplo 1 — requisito fraco vs. requisito executável

**Fraco**

> REQ-007: O sistema deve garantir que o laudo seja conferido antes da liberação.

Por que falha: não diz o que acontece na violação, não diz quem confere, não permite teste.

**Executável**

> REQ-007: Um resultado percorre ENTERED → REVIEWED → RELEASED. Liberar a partir de ENTERED falha com `InvalidTransition`. A liberação registra `released_by` e `released_at`.
>
> Aceitação: (a) liberar sem conferir falha; (b) conferir e liberar conclui com status `released` e revisor registrado.

A diferença não é tamanho: é a existência de uma condição de erro verificável.

## Exemplo 2 — eval declarativo vs. eval executável

**v1 (declarativo)**

```json
{"id": "EVAL-007", "requirement_refs": ["REQ-007"], "layer": "target_system",
 "scenario": "liberação sem conferência", "execution_status": "not_run", "executor": null}
```

**v2 (executável)**

```json
{"id": "EVAL-007", "req": "REQ-007", "layer": "target_system",
 "given": "resultado em ENTERED", "when": "liberação direta", "then": "InvalidTransition",
 "node_ids": ["tests/test_result.py::test_liberacao_sem_conferencia_e_bloqueada"]}
```

O segundo quebra o build quando o comportamento muda. O primeiro só quebra a confiança.

## Exemplo 3 — limite honesto

**Ruim**

> O sistema está pronto para uso em laboratórios.

**Bom**

> A r001 não tem autenticação: `X-Tenant-Id` e `X-Actor` são headers não autenticados. **A API não pode ser exposta à internet neste estado.** Sem IdP não há prova técnica de quem liberou um laudo — risco registrado como RSK-005, pré-requisito do piloto.

## Exemplo 4 — caso real (LIS Aberto, r001)

Pacote construído com esta skill: 19 requisitos, 26 casos de eval em três camadas, 50 testes, 0 requisitos órfãos.

O que fez diferença:

| Decisão | Efeito no pacote |
| --- | --- |
| Invariante negativa por requisito P0 | 21 dos 50 testes verificam o que o sistema **não** faz |
| Relógio injetado | teste de expiração de token em 3 linhas, sem `sleep` |
| Hash canônico documentado | auditor consegue recalcular sem o sistema |
| `out_of_scope` com seis itens | impediu que a fundação virasse MVP pela metade |
| Risco alto declarado (RSK-004/005) | conversa com cliente começa pelo pré-requisito, não pela feature |

O que ficou de fora e por quê: autenticação, UI, TISS, ASTM, assinatura ICP-Brasil, migração de dados. Cada item com consequência escrita, não apenas listado.

## Tom

Direto, sem entusiasmo publicitário. Quando o número é desconhecido, dizer desconhecido. Quando a decisão é opinião, chamar de recomendação. Quando o limite é sério, colocar em negrito — não suavizar.
