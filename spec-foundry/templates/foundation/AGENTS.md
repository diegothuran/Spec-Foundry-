# Regras para a IA construtora do produto alvo

Estas regras orientam a IA que implementará o produto descrito pela fundação. Elas não devem ser copiadas para o runtime como se fossem um processo da skill.

## Princípios obrigatórios

- Construa somente dentro de `{{SCOPE}}` e sinalize qualquer expansão de escopo.
- Trate requisitos, decisões e contratos como fonte de intenção; não invente fatos ausentes.
- Separe evidência observada, inferência, hipótese e decisão aprovada.
- Preserve os vínculos SRC-* -> EVD-* -> CLM-* -> REQ-* -> DEC-* ou TASK-* quando existirem.
- Use `Q-*` para perguntas ainda abertas e `CON-*` para conflitos não resolvidos.
- Não considere uma avaliação passada sem execução e relatório verificável.
- Imagens são referência visual; não deduza backend, banco, permissões ou integrações a partir delas.
- Isole dados, arquivos, logs, configuração e credenciais de cada projeto.
- Nunca peça, armazene ou revele credenciais em artefatos, prompts, fixtures ou relatórios.
- Não assuma Agno, Data Terminal, FastAPI, GCP, Heroku ou qualquer stack específica.
- Registre uma decisão técnica apenas quando a opção tiver sido definida e aprovada.
- Ao faltar informação, abstenha-se de escolher, explique o impacto e abra uma pergunta.
- Respeite `critical`, `high` e `normal` sem transformar severidade em prioridade implícita.
- Mantenha testes do gerador, checks do pacote e evals do target separados.
- Pare e solicite revisão humana para mudanças de recorte, segurança, dados ou comportamento.

## Entrega

Adapte estes templates e remova instruções `[Preencher ...]` antes de entregar. A IA pode propor mudanças, mas somente uma pessoa aprova revisão, recorte, readiness e baseline. Não embarque este fluxo editorial como funcionalidade do produto, salvo se houver requisito explícito para isso.
