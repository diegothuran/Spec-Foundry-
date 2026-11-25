# Spec Foundry v1 → v2: o que mudou e por quê

**Data:** 25/11/2026 · **v1 analisada:** `spec-foundry/` deste repositório (11 referências, 18 templates, schema, 4 scripts, 28 testes) · **v2:** `spec-foundry-v2/`

## Correção de uma análise anterior

A primeira versão desta análise foi feita quando este repositório não estava acessível à sessão de trabalho. Naquele momento eu reconstruí o kit a partir de registros de conversa (8 arquivos, ~49 KB) e concluí que sete referências e os templates tinham se perdido.

**Estavam aqui o tempo todo.** Este documento foi reescrito depois de clonar o repositório e ler os originais. Três afirmações da versão anterior precisam de correção:

| O que eu disse | O que é verdade |
| --- | --- |
| "Sete referências não foram recuperadas" | As 11 referências existem, incluindo `eval-design`, `discovery-and-scope` e `review-and-approval` |
| "Prontidão sem gate objetivo" | A v1 tem condições bloqueantes (Q/CON em aberto) e validador; o que falta é gate ligado a evidência executável, porque não há execução |
| "Eval declarativo por descuido" | É fronteira declarada: `eval-design.md` diz que `target_system` só roda "quando o produto existir e estiver disponível" |

O restante da análise se sustenta na leitura dos originais.

## O que a v1 faz bem

A v1 é um sistema de especificação maduro. A cadeia `SRC → EVD → CLM → REQ` com locators tipados (página, linha, bbox, seção), os três tipos de claim (`user_definition`, `supported_inference`, `proposal`), o schema versionado do modelo e o pacote de 18 templates entregam algo raro: spec que não inventa. `eval-design.md` vai além e exige oráculo não circular, denominador declarado e proibição de transformar comparação do próprio gerador em gold.

Isso não foi descartado na v2 — foi preservado e, em alguns pontos, endurecido.

## Onde a v1 para

O limite é explícito no `SKILL.md`: "Não implementar funcionalidades nem publicar/contratar/deployar serviços por este modo". A consequência prática aparece em três lugares:

1. **Todo eval nasce `not_run`.** O kit tem `init_project.py`, `validate_package.py` e `bundle_project.py` — nenhum executa caso. `executor` e `report_ref` ficam `null` por construção, e nada no pacote pode mudá-los.
2. **Nenhum vínculo com teste de código.** O modelo liga `REQ` a `EVAL` e para aí. Não existe marcador, campo ou ferramenta que ligue requisito a teste real, porque o código não faz parte do escopo.
3. **Assunção não é entidade.** As coleções do modelo são `sources, evidence, claims, requirements, decisions, tasks, risks, questions, conflicts, eval_cases, artifacts, semantic_reviews, approvals`. Não há `ASM-*`. Assunção só existe disfarçada de `proposal`, sem campo de impacto — e é exatamente onde a IA inventa com naturalidade.

Há ainda duas lacunas que não são de escopo, são de manutenção: nada trata do **drift** entre spec e código ao longo do tempo, e o contrato OpenAPI gerado nunca é comparado com o que uma aplicação realmente serve.

## O que a v2 acrescenta

| Lacuna | Mudança |
| --- | --- |
| Proíbe construir | **Modo Fundação**: ordem de construção (domínio → persistência → casos de uso → integração → borda), regra de tamanho e definition of done |
| Eval sem harness | `run_evals.py` executa três camadas e grava relatório; `passed` só existe com JSON de execução |
| Sem vínculo com teste | `@pytest.mark.req("REQ-00X")` + `check_traceability.py` lendo decoradores por AST |
| Prontidão sem evidência executável | Gates G1–G6 no modelo e no validador, incluindo rastreabilidade fechada |
| Sem drift | `references/traceability.md` com rotina de release e sinais de divergência |
| Assunção invisível | `ASM-*` obrigatório, com `impact` exigido pelo validador |
| Contrato não exercitado | Camada `contract` lê o OpenAPI **servido** (`--probe`) e compara com o versionado |

A regra que resume a v2: **evidência é execução**. O que não roda é declarado como limite, não como cobertura.

## Prova de uso

A v2 foi usada para construir uma fundação real de LIS (domínio de laboratório: pedido → amostra → resultado → laudo → auditoria → portal → HL7). Números medidos, não estimados:

| Métrica | Valor |
| --- | --- |
| Requisitos | 19 |
| Casos de eval | 26 (19 `target_system`, 2 `contract`, 5 `static`) |
| Testes | 50, todos marcados por requisito |
| Requisitos órfãos | 0 |
| Evals passando | 26/26 |
| Rotas no contrato | 20, versão 0.1.0 |

Os próprios scripts da v2 validaram o projeto que ela ajudou a produzir: `validate_package.py` → passed; `check_traceability.py` → 19/26/50 com zero órfãos; `run_evals.py --probe lis.api.app:create_app` → 26/26. No caminho, o validador encontrou um defeito real (`REQ-015` sem caminho feliz na aceitação), corrigido no modelo.

## O que a v2 ainda deve à v1

Honestidade sobre o que ficou pior:

- **Sem JSON Schema do modelo v2.** A v1 tem `schemas/project-model.schema.json`; a v2 valida por script, sem schema versionado. Isso é regressão e deve ser corrigido.
- **Sem testes da própria skill.** A v1 tem 28 testes de código e 10 casos comportamentais; a v2 tem validação estrutural, não suíte própria.
- **Sem templates dos cinco anchors.** A v1 entrega 18 templates (produto, requisitos, desenho, plano, configuração de agente); a v2 entrega 6 e delega o resto ao modo fundação.
- **Menos granularidade em evidência.** As referências da v2 foram escritas em menos linhas que as originais; onde a v1 detalha, a v2 resume.

A v2 não substitui a v1: ela cobre o trecho que a v1 deliberadamente não cobre. Quem quer só especificação rigorosa usa `spec-foundry/`. Quem quer especificação que vira código verificável usa `spec-foundry-v2/`.

## Recomendação

1. Trazer o schema JSON da v1 para o modelo v2 e validar com ele.
2. Portar os 28 testes da v1 para cobrir também os scripts da v2.
3. Rodar a v2 em um segundo domínio (financeiro ou jurídico) antes de tratá-la como geral.
4. Manter as duas pastas: versões com escopos diferentes, não uma substituindo a outra.
