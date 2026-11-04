# {{PROJECT_NAME}} — fundação Spec/Eval

[Preencher o objetivo desta fundação, público-alvo e recorte, distinguindo produto especificado de aplicação implementada. Remover as instruções dos templates antes de validar/exportar.]

```yaml
schema_version: 1.0
project_id: {{PROJECT_ID}}
project_name: {{PROJECT_NAME}}
revision: {{REVISION}}
scope: {{SCOPE}}
readiness: {{READINESS}}
```

A primeira revisão deve ser `r001`; `readiness` só pode ser `discovery`, `ready_for_review` ou `approved_baseline`. A aprovação do recorte e da revisão é humana, nunca uma decisão automática de LLM.

[Preencher o que foi efetivamente validado, o que permanece not_run/blocked e as perguntas que impedem avançar. Não declarar produto implantado ou testes runtime executados sem evidência.]

## Ordem recomendada

1. [Product spec](docs/specs/01-product-spec.md)
2. [Requirements](docs/specs/02-requirements.md)
3. [System design](docs/specs/03-system-design.md)
4. [Implementation plan](docs/specs/04-implementation-plan.md)
5. [Agent configuration](docs/specs/05-agent-configuration.md)
6. [Domain model](docs/domain-model.md)
7. [Data contracts](docs/data-contracts.md)
8. [Traceability](docs/traceability.md)
9. [Open questions](docs/open-questions.md)
10. [Assumptions and risks](docs/assumptions-and-risks.md)
11. [ADR template](docs/adr/000-template.md)
12. [Eval spec](evals/eval-spec.md)
13. [Rubrics](evals/rubrics.md)
14. [Review](docs/review.md)
15. [Change impact](docs/change-impact.md)

O artefato de modelo principal será criado pelo projeto em `model/project-model.json`. Os casos de avaliação serão mantidos em `evals/cases.json`, usando JSON da biblioteca padrão escolhida pelo projeto. Esses caminhos são referências de integração, não arquivos opcionais desta pasta.

Preserve isolamento entre projetos, não inclua credenciais e trate imagens como referência visual, sem inferir backend, dados ou integrações que não estejam evidenciados. Não fixe Agno, Data Terminal, FastAPI, GCP ou Heroku como padrão; registre uma escolha somente quando ela estiver definida e aprovada.
