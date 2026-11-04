# Contrato de saída da skill

A skill é o método reutilizável. A pasta gerada é uma fundação específica de projeto. Não copiar anexos de clientes para a skill nem misturar dados de projetos antigos por semelhança de domínio.

## Árvore do projeto gerado

```text
<project-id>-<revision>/
  README.md
  AGENTS.md
  CLAUDE.md
  model/project-model.json
  schemas/project-model.schema.json
  docs/specs/01-product-spec.md
  docs/specs/02-requirements.md
  docs/specs/03-system-design.md
  docs/specs/04-implementation-plan.md
  docs/specs/05-agent-configuration.md
  docs/domain-model.md
  docs/data-contracts.md
  docs/traceability.md
  docs/open-questions.md
  docs/assumptions-and-risks.md
  docs/review.md
  docs/change-impact.md
  docs/adr/
  evals/eval-spec.md
  evals/cases.json
  evals/rubrics.md
  evals/fixtures/           # somente fixtures criadas e autorizadas
  evals/reports/            # somente relatórios realmente executados
  scripts/common.py
  scripts/validate_package.py
  scripts/bundle_project.py
  manifest.json            # criado no momento de exportar, não por template
  sources/                 # originais privados locais, fora do ZIP padrão
```

Core mínimo é a lista `CORE` de `scripts/common.py`. O scaffold inclui os scripts portáteis no projeto para que a próxima IA possa repetir os checks sem instalar a skill. `docs/adr/000-template.md` é ponto de partida; preencher como ADR real, substituir por ADRs numeradas e atualizar links, ou documentar N/A/remover arquivo e seu link/registro quando não houver decisão material.

O modelo desta skill é JSON Schema, mas não é schema de domínio do sistema-alvo. Contratos específicos, OpenAPI, exemplos, configs e prompts só entram se houver definição suficiente. Colocar em subpastas próprias e registrar em artifacts. Não gerar contratos de negócio com dados/enum inventados por necessidade de volume.

## Papel dos cinco anchors

Product: objetivo, atores, jornadas, valor, recorte e fora de escopo. Requirements: comportamentos e restrições rastreáveis com critérios observáveis. Design: componentes, contratos, dados, estados, segurança e alternativas. Plan: cards de levantamento/POC/implementação com gates e dependências. Agent configuration: limites da IA implementadora e, se relevante, regras da IA do produto.

A organização segue os cinco anchors usados nesta conversa; não alegar certificação por um padrão externo chamado Evan Spec. Eval specs são camada explícita adicional. Não copiar a arquitetura do gerador para todo produto que ele descreve.

## Conteúdo final, não template preenchido parcialmente

Eliminar marcadores `{{...}}` e orientações `[Preencher ...]`. Reescrever introduções dos templates para falar do projeto. Quando algo não se aplica, usar N/A e racional; quando falta decisão, usar pergunta/assunção clara. Não remover lacuna simplesmente para o validador passar.

`README.md` deve explicar projeto/recorte, readiness e leitura inicial. Declarar verificações executadas e não executadas. Um projeto em discovery pode ser entregue com lacunas explicitadas e estrutura completa; scaffold vazio não é resultado concluído.

Manter o enunciado completo de cada requisito ativo no documento de requisitos; referências não substituem enunciado. Mapear IDs em artifacts e traceability. O check de texto/IDs não prova equivalência semântica da arquitetura/contrato: comparar as seções manualmente com modelo/fontes.

## Export e fontes privadas

Registrar apenas arquivos que pretende compartilhar em artifacts; allowlist não prova que o conteúdo é seguro. Revisar PII/segredos antes de exportar. O bundler rejeita `.env`, certificados/chaves e arquivos de sources, mas não é um scanner DLP nem garante ausência de dados sensíveis em Markdown.

O ZIP não contém originais locais privados. Modelo pode manter referências e hashes; o destinatário verá advertência de que originais não estão disponíveis e precisa recebê-los por canal autorizado para verificar grounding. Trechos citados também podem conter dados pessoais: minimizar/redigir de modo explícito, sem alterar indevidamente o fato que sustentam.

Usar `validate_package.py --exported` após extrair o ZIP para conferir arquivos/hashes do manifest sem fingir verificação dos originais excluídos. Sem `--exported`, o verificador exige os originais locais registrados. O manifest não autentica o autor nem a aprovação.

## Prontidão e atualização

Discovery mantém questões/conflitos e evidências incertas explícitos. Ready_for_review permite revisão humana, não implementação incondicional. Approved_baseline exige revisão humana e aprovação explícita da revisão/recorte; é prontidão da especificação, não release do produto.

Preservar arquivos anteriores em nova pasta r002 etc.; copiar fontes quando autorizado ou manter references não locais declaradas. Não usar aprovação de r001 para r002. Documentar IDs adicionados/alterados/removidos e efeito nos contratos/tasks/evals. Não renumerar tudo para tornar diff artificialmente limpo.

O padrão não inclui servidor, fila cloud, multiusuário, storage remoto ou API de aprovação. Serviços externos são necessidades do produto-alvo quando definidas, não dependências obrigatórias de geração.
