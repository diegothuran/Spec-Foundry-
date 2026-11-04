# Revisão e aprovação

## Finalidade

A revisão verifica semântica, rastreabilidade e limites do recorte antes de congelar uma baseline.

Ela não substitui validação do produto, autenticação ou auditoria imutável.

A aprovação deve ser explícita na conversa; silêncio, emoji ou ausência de objeção não bastam.

O escopo precisa estar congelado no momento da aprovação.

## Registro de revisão

O ProjectModel mantém `semantic_reviews` como lista de registros.

Cada registro usa `{revision, scope, reviewer, kind, result, notes, evidence_ref}`.

`kind` aceita `human` ou `llm`.

`result` aceita `pass`, `fail` ou `needs_changes`.

Use `evidence_ref` para ancorar observações em uma evidência locável quando aplicável.

Uma revisão de LLM é análise auxiliar, não aprovação humana.

## Registro de aprovação

O ProjectModel mantém `approvals` como lista de registros.

Cada registro usa `{revision, scope, actor, decision, evidence_ref}`.

`decision` aceita `approve` ou `reject`.

`evidence_ref` de aprovação aponta somente para `EVD` humano apoiado em `user_message`.

Esse apoio precisa registrar a frase, o turno ou outra localização recuperável da mensagem.

Anexo, saída MCP e inferência do modelo não são evidência de autorização.

Os registros locais são declarativos; não constituem autenticação nem auditoria imutável.

## Portões

Antes da revisão, valide schema, refs, perguntas, conflitos e legibilidade das fontes relevantes.

Não declare `ready_for_review` com `Q` blocking `open`.

Não declare `ready_for_review` com `CON` blocking `open`.

Não declare `ready_for_review` se evidência essencial estiver ilegível no recorte.

Para `approved_baseline`, exija revisão compatível e aprovação humana explícita.

A aprovação de uma revisão não autoriza automaticamente outra revisão ou outro scope.

Qualquer mudança em scope ou revision invalida aprovações anteriores.

Após mudança, retorne ao estado de descoberta ou revisão conforme o impacto.

## Resultado

Registre notas sobre pontos aceitos, rejeitados, condicionais e pendentes.

Ligue cada requisito aceito às decisões aprovadas da mesma revisão.

Mantenha decisões propostas visivelmente separadas das decisões aprovadas.

Se o revisor pedir mudanças, preserve o registro e crie nova revisão; não sobrescreva o histórico local.

Um relatório de avaliação pode apoiar a revisão, mas não substitui a decisão humana exigida.
