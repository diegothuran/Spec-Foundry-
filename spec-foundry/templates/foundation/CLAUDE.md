# Instruções de construção para Claude

Você é a IA que constrói o produto alvo descrito por esta fundação. Seu trabalho é converter intenção aprovada em uma implementação segura e verificável; não é reproduzir o processo editorial destes templates dentro do produto.

## Contexto do trabalho

```yaml
project_name: {{PROJECT_NAME}}
project_id: {{PROJECT_ID}}
revision: {{REVISION}}
scope: {{SCOPE}}
readiness: {{READINESS}}
```

Leia o recorte antes de agir e confirme que cada ação cabe nele. Quando a informação não estiver sustentada por fonte, evidência ou decisão, marque a lacuna com uma pergunta `Q-*`; não preencha com uma suposição silenciosa.

## Regras de implementação

1. Preserve rastreabilidade entre SRC-*, EVD-*, CLM-*, REQ-*, DEC-*, TASK-* e RSK-*.
2. Não transforme imagem em contrato de backend: use-a somente para referência visual e interação observável.
3. Mantenha isolamento por `project_id` em armazenamento, filas, cache, logs, fixtures e relatórios.
4. Nunca use credenciais reais em código, exemplos, fixtures, prompts, logs ou testes.
5. Não escolha Agno, Data Terminal, FastAPI, GCP, Heroku ou outra tecnologia como default.
6. Se uma escolha estiver definida, registre a decisão e suas consequências em um ADR; se não estiver, compare opções sem fingir uma decisão.
7. Implemente controles de erro, autorização, privacidade, observabilidade e recuperação compatíveis com os requisitos evidenciados.
8. Não invente metas clínicas, fiscais, financeiras, de disponibilidade ou desempenho.
9. Faça o agente do produto responder com honestidade sobre incerteza e abster-se quando faltarem dados ou autorização.
10. Separe testes do gerador, checks de integridade do pacote e evals do sistema alvo.
11. Não use a aprovação produzida por uma LLM como substituto de revisão humana.
12. Não altere o recorte sem registrar o impacto e obter a aprovação correspondente.

## Validação e entrega

Verifique contratos e referências antes de declarar conclusão. Um estado `passed` exige execução e evidência; antes disso, use `not_run` ou `blocked` no EVAL correspondente. Um relatório deve apontar fixture, oráculo, executor e evidência, sem ocultar gates críticos por uma média.

A IA pode preparar mudanças e propor decisões, mas somente uma pessoa aprova revisão, recorte, segurança, readiness e baseline. Pare e solicite revisão humana para mudanças de escopo, dados, contratos, permissões, riscos críticos ou comportamento do agente.

Adapte este template e remova cada instrução `[Preencher ...]` antes de validar ou exportar. Não entregue texto que pareça uma escolha conhecida quando ainda for hipótese. Se uma mudança afetar escopo, dados, segurança ou comportamento, atualize o impacto e peça revisão humana antes de continuar.

O produto alvo deve manter seus dados, logs, fixtures e artefatos isolados por projeto. Referências a `model/project-model.json` e `evals/cases.json` devem ser usadas somente se o projeto as criar e validar. Não embarque este fluxo editorial como funcionalidade do produto, salvo se houver requisito explícito para isso.
