# Spec Foundry — skill para Claude

Skill para transformar definições de projetos em texto, imagens e PDFs em uma fundação rastreável de specs e eval specs para outra IA implementar. Não implementa o produto-alvo, não escolhe stack por herança e não transforma testes planejados em resultados aprovados.

A skill está em [`spec-foundry/`](spec-foundry/). O [guia de montagem](GUIA-MONTAGEM.md) explica instalação no Claude de navegador e Claude Code, prompts de uso e manutenção. Veja também as [verificações locais](CHECKS-LOCAIS.md).

## Conteúdo

- `spec-foundry/SKILL.md`: fluxo e ativação da skill.
- `spec-foundry/references/`: evidências, discovery, contratos, evals, aprovação, revisões e guardrails.
- `spec-foundry/templates/`: 18 templates Markdown de fundação e modelo canônico.
- `spec-foundry/schemas/`: contrato do modelo da skill.
- `spec-foundry/scripts/`: scaffold, checks locais e exportação.
- `tests/`: 28 testes locais e 10 casos comportamentais do Claude ainda `not_run`.
- `tooling/`: geração do schema e dos ZIPs de distribuição.

## Instalar no Claude Code

Copie a pasta `spec-foundry/` inteira para `~/.claude/skills/spec-foundry/` ou para `.claude/skills/spec-foundry/` no repositório desejado. Não sobrescreva uma instalação editada sem backup.

Depois, use:

```text
/spec-foundry Analise estes materiais e gere a fundação do projeto.
Primeiro consolide o entendimento e as perguntas bloqueantes. Não implemente o sistema.
```

## Gerar o ZIP para o Claude de navegador

Com Python 3.10+ disponível, na raiz deste repositório:

```bash
python3 -m unittest discover -s tests -v
python3 tooling/package_kit.py --output-dir ./dist
```

Envie **`dist/spec-foundry-claude.zip`** em **Customize > Skills > Upload a skill** e ative a skill. Criação/edição de arquivos e execução de código precisam estar habilitadas na conta. O outro ZIP, `dist/claude-spec-foundry-kit.zip`, é o kit de manutenção, não o arquivo de instalação.

O empacotador não sobrescreve versões existentes. Preserve os ZIPs anteriores e use uma pasta externa nova para uma nova distribuição, ou limpe `dist` conscientemente depois de salvar os artefatos.

## Prontidão e segurança

`discovery`, `ready_for_review` e `approved_baseline` são estados da especificação, não do release do software. Aprovação exige evidência humana explícita na mesma revisão/recorte. Os registros locais não são identidade autenticada ou auditoria imutável.

Checks locais validam contratos e referências; não comprovam grounding, qualidade multimodal ou execução de testes do alvo. Os 28 testes de código passaram no ambiente de criação. Instalação e comportamento no Claude precisam ser testados na conta em uso; os 10 casos comportamentais continuam `not_run`.

Não guardar projetos/clientes, anexos, segredos ou certificados na pasta da skill. Os exemplos dos testes são sintéticos. A leitura de PDF/imagem, pesquisa e MCP dependem das ferramentas disponíveis, não são serviços fornecidos pelos scripts.

## Desenvolvimento

Os scripts da skill usam apenas a biblioteca padrão do Python. Para alterar o modelo, mantenha schema, validadores, templates e testes coerentes; use `python3 tooling/build_model_schema.py` para materializar o contrato versionado. Não renomeie ou remova requisitos/casos apenas para os checks passarem.

Versão inicial: **1.0.0**. É uma skill independente, não um plugin ou SaaS implantado.
