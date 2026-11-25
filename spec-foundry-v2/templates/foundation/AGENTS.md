# Instruções para a IA implementadora

Este projeto usa Spec Foundry v2. Antes de escrever código:

1. Ler `foundation/{{release}}/model/project-model.json` e as specs em `docs/specs/`.
2. Implementar apenas requisitos com `priority` P0/P1 e caso de eval associado.
3. Marcar cada teste com `@pytest.mark.req("REQ-00X")`.
4. Rodar `python3 scripts/check_traceability.py --project .` e `python3 scripts/run_evals.py --project .` antes de dizer que terminou.
5. Não alterar requisito para acomodar código. Se o requisito está errado, registrar decisão e atualizar o modelo.

Proibido: declarar teste passando sem executar; usar `TODO`/`TBD` em artefato normativo; expor endpoint sem isolamento por tenant.
