# Descoberta e escopo

## Propósito

A descoberta converte evidências em um recorte verificável para foundations de projeto.

A abordagem usa cinco anchors de projeto: `product`, `requirements`, `design`, `plan` e `agent config`.

São anchors usados na conversa e em especificações de avaliação; não são um padrão certificado.

Não presumir que o nome Evan, ou qualquer nome semelhante, seja uma taxonomia oficial.

## ProjectModel

O núcleo usa `schema_version: 1.0`.

Campos mínimos: `project_id`, `name`, `revision`, `scope` e `readiness`.

A revisão inicial é `r001`.

`readiness` aceita `discovery`, `ready_for_review` e `approved_baseline`.

O grafo de rastreabilidade é `SRC -> EVD -> CLM -> REQ -> DEC/TASK/RSK/EVAL`.

`Q` representa perguntas e `CON` representa conflitos; ambos devem ser localizáveis.

## Procedimento

Comece delimitando objetivo, usuários, entradas, saídas e não-objetivos.

Mapeie cada informação para um ou mais anchors, sem forçar uma informação ambígua em um único anchor.

Diferencie comportamento desejado, restrição observada e hipótese de implementação.

Crie `REQ` com status `proposed`, `accepted` ou `deferred`.

Todo requisito tem prioridade `critical`, `high` ou `normal`.

Um `REQ` `accepted` exige `decision_refs` apontando para `DEC` aprovada por humano relativa à mesma revisão.

Uma decisão proposta continua sendo proposta, mesmo que pareça óbvia ou venha de documento anexado.

Registre `Q` com status `open`, `answered` ou `deferred`.

Marque perguntas como blocking quando a resposta puder mudar escopo, segurança ou aceitação.

Registre `CON` com status `open` ou `resolved`.

Marque conflitos como blocking quando duas interpretações alterarem o resultado esperado.

## Portão de escopo

O escopo deve declarar o que está dentro, fora e condicionado a resposta ou ferramenta.

O recorte de revisão precisa identificar `project_id`, revisão e anchors envolvidos.

Não declarar `ready_for_review` enquanto houver `Q` ou `CON` blocking em aberto.

Também bloqueia prontidão qualquer evidência ilegível relativa ao recorte.

Se uma ferramenta essencial estiver indisponível, registre a limitação como risco ou pergunta blocking.

`ready_for_review` significa preparado para avaliação humana, não aprovado.

A aprovação exige detecção explícita em conversa e escopo congelado.

Mudança de escopo ou revisão invalida aprovações anteriores.

## Saídas de descoberta

Entregue um resumo de contexto em arquivo, com fontes, decisões propostas e lacunas.

Inclua mapa de anchors e a cadeia de referências até cada requisito importante.

Separe `DEC` proposta de `DEC` aprovada e não use proposta como fato.

Derive tarefas somente quando houver base suficiente e assinale dependências.

Registre riscos operacionais, de segurança, de domínio e de dados como `RSK`.

Defina quais avaliações serão especificadas, sem alegar que o produto já foi executado.

O fim da descoberta é um estado retomável, não uma promessa de implementação.
