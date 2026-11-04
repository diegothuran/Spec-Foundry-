# Exemplos operacionais

Os exemplos são padrões de raciocínio, não dados de cliente e não decisões pré-aprovadas.

## 1. Portal de documentos com retenção pendente

A conversa informa um portal e menciona retenção, mas não define prazo ou autoridade.

Registre o portal como `SRC` e a menção como `EVD` locável.

Crie `REQ` `proposed`, prioridade `high`, e uma `Q` blocking sobre retenção e jurisdição.

Não invente política de retenção nem marque o projeto como pronto.

O estado correto é `discovery`, não `ready_for_review`.

## 2. Screenshot não prova login ou API

Uma imagem mostra uma tela aparentemente autenticada.

Ela pode sustentar uma observação visual sobre elementos realmente medidos.

Não prova que exista login funcional, API, permissão, backend ou integração.

Crie uma `CLM` limitada e um `RSK` sobre capacidade não observada.

Peça evidência adicional ou marque o requisito como não demonstrado.

## 3. Conflito entre leitura e escrita

Um requisito pede apenas leitura, enquanto uma decisão proposta menciona escrita.

Registre ambos como evidências distintas e crie `CON` blocking com status `open`.

Não escolha escrita por parecer mais completa e não trate a proposta como fato.

Após decisão humana explícita, marque o conflito como `resolved` e derive o requisito correto.

Sem resolução, o recorte permanece em `discovery`.

## 4. Mudança de revisão

A revisão `r001` foi aprovada para um scope que cobre somente o anchor `product`.

Depois, o usuário acrescenta API e altera o anchor `agent config`.

Crie `r002`, registre a mudança e invalide as aprovações de `r001` para o novo recorte.

Reavalie requisitos, avaliações, perguntas e riscos afetados.

Não copie a aprovação antiga para `r002`.

## 5. Bloqueio de MCP

Uma avaliação depende de um resultado MCP, mas a ferramenta está indisponível.

Mantenha `fixture_ref: null`, `executor: null` e `status: blocked` ou `not_run`.

Registre a dependência como `Q` ou `RSK`, conforme a natureza do bloqueio.

Não fabrique resposta MCP nem execute `target_system` sem produto implementado.

Quando a ferramenta voltar, reavalie a revisão e a aplicabilidade do caso.

## Resumo comum

Em todos os casos, preserve a cadeia `SRC -> EVD -> CLM -> REQ -> DEC/TASK/RSK/EVAL`.

Use referências locáveis, explicite incerteza e mantenha a aprovação humana separada.

O arquivo de contexto permite retomar o trabalho sem presumir memória da conversa.
