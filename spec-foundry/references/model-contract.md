# Contrato do modelo — versão da skill 1.0

Usar `schemas/project-model.schema.json` como contrato estrutural e `model/project-model.json` de cada projeto como snapshot. Este é um perfil leve para arquivos locais, não o schema anterior do SaaS; migração entre perfis exige mapear campos/versões explicitamente.

## Metadados e coleções

Exigir `schema_version: "1.0"`, `project_id` slug, `project_name`, `revision` como `r001`, `scope`, `language` e `readiness`. Congelar revisão/recorte quando submeter para aprovação. Não confiar em nome igual para identificar projeto.

Todas as coleções existem, mesmo quando vazias: sources, evidence, claims, requirements, decisions, tasks, risks, questions, conflicts, eval_cases, artifacts, semantic_reviews e approvals. Coleção vazia não demonstra que houve investigação; explicar N/A ou pendência nos documentos.

Fonte `SRC-*`: kind text/user_message/pdf/image/web/mcp; label e ref localizável; local_path relativo ao projeto ou null; sha256 dos bytes ou null. SHA-256 exige arquivo real. Original em sources é privado e não é exportado por padrão. Texto copiado de conversa deve ser identificado como transcrição, não evidência de identidade autenticada.

Evidência `EVD-*`: source_ref, quote ou null, locator e quality clear/uncertain. Locator tem kind e ref; text_lines exige lines [início,fim] 1-based; pdf_page exige page >= 1; image_region exige bbox [x0,y0,x1,y1] normalizada e ordenada; web_section usa URL/seção; user_message usa mensagem/transcrição identificável; mcp_record usa ref de registro. Não usar bbox quando não medido: marcar incerteza e descrever limitação fora do modelo até obter região válida.

Claim `CLM-*`: text, kind user_definition/supported_inference/proposal e evidence_refs. As duas primeiras exigem evidência. Proposal sem evidência é recomendação, não fato. Evidência existente mas irrelevante falha semanticamente.

Requisito `REQ-*`: statement, priority critical/high/normal, status proposed/accepted/deferred, claim_refs, decision_refs. Ativo significa proposed/accepted no recorte. Todo ativo precisa claim, task, eval de target_system e referência no documento de requisitos. Accepted exige decisão approved na mesma revisão/escopo, vinculada ao requisito e a evidência de resposta humana clara.

Decisão `DEC-*`: statement, rationale, status proposed/approved/rejected, revision, scope, requirement_refs e evidence_ref. Proposed pode ter evidence_ref null. Approved exige evidência humana; nenhuma sugestão do gerador é aprovação implícita. Decisão arquitetural não necessariamente referencia requisito, mas deve ser explicada em ADR/documento.

Tarefa `TASK-*`: title, kind discovery/poc/implementation, requirement_refs, dependency_refs e acceptance. Dependências devem existir, não ser a própria tarefa e não criar ciclo. Detalhar o card no plano.

Risco `RSK-*`: description, severity, requirement_refs e mitigation. Mitigation não é prova de eliminação do risco. Cobrir com avaliação pertinente quando ligado a requisito crítico.

Pergunta `Q-*`: text, blocking, status open/answered/deferred e evidence_ref. Answered exige evidência humana; pergunta blocking deferred ainda bloqueia revisão enquanto estiver no recorte. Para tirá-la do recorte, registrar decisão e novo escopo, não mudar somente status.

Conflito `CON-*`: description, claim_refs, blocking, status open/resolved e resolution_evidence_ref. Exigir pelo menos duas claims conflitantes. Resolved exige evidência clara e racional nos documentos; não eliminar a fonte contraditória.

## Evals e arquivos

Eval `EVAL-*`: layer generator/package/target_system; requirement_refs; scenario, input, expected; oracle com kind deterministic/human/runtime/llm_judge e description; severity; fixture_status missing/synthetic/curated; fixture_ref; executor; execution_status not_run/blocked/passed/failed; report_ref.

Fixture missing implica fixture_ref null. Fixtures declaradas synthetic/curated exigem arquivo local real. Não transformar fixture sintética em gold validado por renomear. Casos futuros têm executor e report_ref null, status not_run. Blocked explicita pré-requisito ausente. Passed/failed exigem executor, arquivo de relatório e evidência de execução; somente campos preenchidos não provam execução real.

O relatório referenciado por um caso executado deve ser JSON com layer igual ao caso, revision igual ao modelo, case_ids incluindo o caso, status igual ao caso, executor igual ao caso, evidence_refs com arquivos locais reais e limitations não vazias. Checks locais da skill não podem servir como relatório target_system. O verificador checa essa estrutura; o leitor humano confirma a execução.

Artifact: path relativo seguro, requirement_refs e eval_refs. Registrar todos os arquivos que pretende exportar, inclusive modelo/schema/evals. Não registrar originais em sources. Manifest não registra/hash de si mesmo; é gerado à parte. Arquivo criado mas não registrado não é exportado.

`evals/cases.json` é uma lista exatamente igual a `eval_cases`. Não alterar manualmente apenas uma cópia. Documents e JSON devem refletir o mesmo significado; os scripts verificam apenas parte dessa equivalência.

## Revisão e aprovação locais

SemanticReview: revision, scope, reviewer, kind human/llm, result pass/fail/needs_changes, notes e evidence_ref. Revisão humana exige evidência da resposta do usuário; revisão LLM pode ajudar, não é independente por padrão.

Approval: revision, scope, actor, decision approve/reject e evidence_ref. Exigir fonte user_message e evidência clear. Para approved_baseline, ter última aprovação da revisão/escopo em approve e última revisão humana em pass; revisão mais nova pedindo alterações invalida prontidão.

O script também impede ready_for_review/approved_baseline com pergunta/conflito blocking não resolvido ou evidência incerta em requisito ativo. Não verifica identidade, não assina aprovação nem impõe permissão multiusuário; os registros locais são declarações para revisão, não auditoria imutável.

## Limite de validação

O validador portátil implementa somente o subconjunto de JSON Schema usado pelo schema fornecido e invariantes locais adicionais. Não se apresenta como validador universal de OpenAPI/JSON Schema. Usar ferramentas especializadas para contratos de produto-alvo. Evidência textual, normativas, pertinência clínica/jurídica e equivalência semântica exigem ferramentas/revisão apropriadas.
