# Verificações locais — Spec Foundry 1.0.0

Em 04/11/2026 foram executados **28 testes unitários/integrados locais** de `tests/test_skill.py`, todos com resultado OK. Eles usam inputs/atores/declarações sintéticos; não são sessões do Claude nem aprovações reais de projeto.

Os testes incluem scaffold vazio corretamente incompleto, modelo discovery válido, ID/ref/hash/quote incorretos, caminhos inseguros/symlinks, tentativa de exportar `.env`, aceitação sem decisão humana, prontidão com bloqueios, aprovação de revisão errada, rejeição posterior, cobertura target_system, criticidade, resultado sem relatório, relatório de camada errada, fixture inexistente, ciclo de tarefa, divergência de cases/modelo, marcador não resolvido, bbox invertida e export sem originais com verificação de manifest.

Também foram verificadas a sintaxe dos scripts Python, links Markdown locais, campos/limites do frontmatter, schema JSON Schema Draft 2020-12 e um modelo sintético por um validador formal disponível no ambiente de criação. O validador da skill passou no check de estrutura do pacote de skill. Essa ferramenta local não é certificação/instalação pelo Claude.

A skill contém 35 arquivos: 29 Markdown, um schema JSON, um template de modelo JSON e quatro scripts Python. São 18 templates Markdown de fundação e 10 referências Markdown, além de `SKILL.md`.

`tests/behavior-cases.json` contém **10 casos comportamentais, todos not_run**. Estão pendentes: upload/ativação real na conta do Claude, extração multimodal em exemplos anotados, calibração semântica, qualidade das fundações produzidas, revisão humana independente e uso em domínios sensíveis. Os testes de PDF/imagem exigem fixtures reais inofensivas ainda não preparadas neste kit.

Nenhuma instalação no Claude, chamada LLM, leitura de anexos de clientes, conexão MCP, compra, publicação, deploy ou criação de produto-alvo foi executada. Nenhum resultado de `local_contract_checks` pode ser usado como prova de aprovação semântica ou de execução das evals do produto.

Para repetir os testes de código local, execute no kit:

```bash
python3 -m unittest discover -s tests -v
```

Para empacotar, execute `tooling/package_kit.py` e use os arquivos separados de instalação e manutenção conforme o guia. Os hashes e a integridade dos ZIPs verificam conteúdo, não autenticidade/autoria nem correção de requisitos.
