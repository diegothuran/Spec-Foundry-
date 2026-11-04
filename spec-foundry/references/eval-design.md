# Desenho de avaliações

## Escopo

Avaliações descrevem como verificar foundations e produtos sem confundir contrato local com validade do domínio.

As especificações ficam em `evals/cases.json` e `evals/eval-spec.md`.

Use JSON para os casos; não use YAML, evitando dependências desnecessárias.

`evals/eval-spec.md` explica intenção, camadas, oráculos, rubricas e interpretação.

A skill pode gerar essas especificações, mas não deve fingir que executou o target.

## Modelo de caso

Cada caso declara `layer`: `generator`, `package` ou `target_system`.

`generator` testa transformação e decisões geradas pela skill.

`package` testa estrutura, referências e empacotamento dos artefatos.

`target_system` testa o produto implementado, somente quando ele existir e estiver disponível.

`fixture_status` aceita `missing`, `synthetic` ou `curated`.

`fixture_ref` é `null` por padrão e só recebe uma referência existente e autorizada.

`executor` é `null` até haver executor configurado e autorizado.

`report_ref` é `null` antes de um relatório de execução válido.

`status` aceita `not_run` ou `blocked` no planejamento inicial.

Execução real só pode mudar o estado quando houver produto, fixture e executor adequados.

## Oráculos

Oráculos devem ser independentes do mesmo erro que produziu a saída avaliada.

Use gold humano ou holdout quando a tarefa exigir julgamento sem circularidade.

Rubricas devem explicitar critérios, evidência esperada e níveis de resultado.

Critérios de schema e refs são `local_contract_checks`.

Esses checks não provam grounding, segurança clínica, conformidade legal ou validade contábil.

Não transforme uma comparação textual do próprio gerador em gold.

Registre fonte, versão e escopo do gold, quando houver autorização para fazê-lo.

## Métrica e interpretação

Declare denominador para cada taxa, incluindo casos excluídos.

Marque `N/A` quando um caso não for aplicável; não conte `N/A` silenciosamente como acerto.

Explique como casos bloqueados afetam a leitura do relatório.

Risco crítico não pode ser diluído por muitos casos triviais.

Separe falha de geração, falha de empacotamento e falha do target.

Uma suíte pequena pode ser útil, desde que seus limites sejam explícitos.

Não declare validade geral com base apenas em checks locais.

## Bloqueios

Sem produto implementado, casos de `target_system` ficam não executados ou bloqueados.

Sem fixture, mantenha `fixture_status: missing` e não invente conteúdo.

Sem ferramenta habilitada, registre a dependência e preserve `executor: null`.

Sem gold humano ou holdout adequado, reduza a alegação do teste e registre a limitação.

Uma aprovação de revisão não substitui execução, e execução não substitui aprovação humana.

Cada caso deve apontar para requisitos, decisões e evidências pertinentes quando disponíveis.

Mudança de revisão ou escopo exige reavaliar a aplicabilidade dos casos.

A especificação deve ser legível por humanos e validável por ferramentas simples.
