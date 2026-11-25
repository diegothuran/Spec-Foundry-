# Discovery e recorte

## Quatro perguntas de abertura

1. Que decisão o pacote precisa habilitar? (contratar, construir, vender, aprovar orçamento)
2. Quem usa o sistema e quem paga por ele? (quase nunca é a mesma pessoa)
3. Qual o menor recorte que já entrega valor verificável?
4. O que está explicitamente fora — e quem decidiu isso?

Sem resposta para 4, o escopo não existe. Toda spec sem `out_of_scope` cresce até virar impossível.

## Definition of ready

Um pacote só entra em `ready_for_review` quando:

| Gate | Critério objetivo |
| --- | --- |
| G1 | `out_of_scope` não vazio e coerente |
| G2 | todo `REQ` com `acceptance` (feliz + erro) |
| G3 | todo `EVAL` com camada executável e alvo existente |
| G4 | rastreabilidade sem violação |
| G5 | decisão material com ADR e alternativas |
| G6 | risco com mitigação e status |

Enquanto um gate falha, o status é `discovery`. Não existe "pronto com ressalva" — existe pronto ou lista de pendência.

## Perguntas bloqueantes

- Máximo de 3 por rodada, de alto impacto.
- Cada uma com: pergunta, por que bloqueia, o que muda se a resposta for A ou B.
- Continuar o trabalho independente enquanto a resposta não chega.
- Pergunta respondida vira `DEC-*` com evidência da resposta (transcrição), nunca "ficou combinado".

## Conflito entre fontes

Quando duas fontes discordam, registrar `CON-*` com as duas claims. Não escolher silenciosamente a mais conveniente. Conflito bloqueante impede prontidão até ser resolvido com evidência.

## Priorização

| Prioridade | Critério |
| --- | --- |
| P0 | sem isso o sistema é inseguro, ilegal ou inútil |
| P1 | sem isso o usuário principal não trabalha |
| P2 | melhora mensurável, adiável sem quebrar o núcleo |

A fundação implementa P0 inteiro e parte do P1. P2 fica no plano, não no código.

## Recorte por release

`r001` deve ser a menor fatia que prova o domínio de ponta a ponta. Recorte bom tem começo e fim visíveis: "do pedido ao laudo" é recorte; "gestão laboratorial" é tema.

## Sinal de recorte errado

- A release precisa de três integrações para fazer sentido.
- Nenhum requisito pode ser demonstrado sem dado real de cliente.
- O pacote tem mais de 25 requisitos P0 (provavelmente são P1 disfarçados).
- O fora de escopo é maior que o dentro, e mesmo assim a entrega parece impossível.
