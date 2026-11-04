# Ferramentas locais da skill

Os scripts usam somente a biblioteca padrão do Python 3.10+. Não chamam LLM, não usam rede, não instalam dependências nem executam conteúdo de anexos. São apoio à execução autorizada do Claude, não um serviço autônomo.

Localizar `SKILL_DIR` na superfície em uso: pasta real da skill no Claude Code ou extração disponibilizada pelo Claude no chat. Não assumir `/home/ubuntu` nem caminho de outra máquina. Os exemplos abaixo usam bash; no Windows usar o comando Python disponível e caminhos adequados. Na interface de chat, pedir ao Claude que localize e execute os scripts, não tentar executar comandos em um campo de texto.

## Inicializar

```bash
python3 "$SKILL_DIR/scripts/init_project.py" \
  --name "Portal de documentos" \
  --project-id "portal-documentos" \
  --scope "POC de visualização privada" \
  --output "./projects/portal-documentos/r001"
```

A saída precisa ser nova e ficar fora da skill. O script copia templates e cria modelo/cases vazios. O estado discovery e o texto de saída dizem explicitamente que é scaffold; validação deve falhar enquanto não houver fontes, claims, requisitos, tarefas, casos e documentos realmente preenchidos. Não preencher placeholders apenas com texto genérico.

## Validar

```bash
python3 "$SKILL_DIR/scripts/validate_package.py" \
  --project "./projects/portal-documentos/r001" \
  --report "./checks/portal-documentos-r001.json"
```

Saída 0 significa contratos locais passaram; saída 1 indica falha. Relatório precisa de caminho novo. Se colocar relatório em pasta de projeto e quiser exportá-lo, adicioná-lo a artifacts após execução; não usar esse relatório como passed de um caso target_system. O verificador não altera readiness do modelo.

Checks incluem schema do perfil fornecido, IDs, refs, hashes/quotes de texto local quando disponível, locators, dependências, cobertura de tasks/evals, acordo entre cases e modelo, placeholders, caminhos, links locais e gates declarativos de revisão. Existem verificações semânticas não automatizadas: pertinência de fonte, suficiência do oracle, fidelidade das demais seções e validade jurídica/clínica.

O mini-engine suporta somente as keywords usadas no schema incluído. Qualquer contrato novo que use keywords fora desse perfil requer validador especializado/migração, não remover constraints para aparentar conformidade. O schema do projeto deve ser a mesma versão fornecida pela skill.

## Exportar

```bash
python3 "$SKILL_DIR/scripts/bundle_project.py" \
  --project "./projects/portal-documentos/r001" \
  --output "./exports/portal-documentos-r001.zip"
```

O ZIP precisa ser novo e ficar fora da pasta de projeto e da skill. O script falha se houver erro estrutural ou manifest anterior. Preservar snapshot exportado; alterações exigem nova pasta/revisão. Gera manifest com hashes/tamanhos, limites dos checks e estado declarado. Exporta só artifacts registrados e manifest; sources privadas ficam de fora.

Antes de exportar, rever dados pessoais/segredos, não depender da filtragem de extensões. Links para arquivos não exportados devem ser substituídos por referência textual com limitação ou incluir apenas cópia autorizada em pasta distinta; não contornar a exclusão de originais privados.

## Verificar um pacote recebido

```bash
python3 "./portal-documentos-r001/scripts/validate_package.py" \
  --project "./portal-documentos-r001" --exported
```

`--exported` exige manifest e verifica hashes/arquivos/revisão. Se original privado foi excluído, informa limitação de verificação da citação/hash original. Não trocar esse aviso por verificado. Essa verificação não comprova autoria, assinatura ou aprovação legítima.

## Sem Python ou permissões

Não solicitar liberação ampla de shell por padrão. Se runtime bloquear scripts, usar Markdown/modelo e revisão manual, registrando checks e export não executados. Não gravar relatórios de pass sem execução. Pesquisa web, OCR e MCP são capacidades separadas e não passam a existir porque a skill foi instalada.

## Ordem de uso

Inicializar scaffold → analisar fontes → preencher modelo → gerar documents/cases → comparar semântica → executar checks → revisar com humano → registrar estado/evidência → revalidar → exportar. Mudança após aprovação exige nova revisão; script não autentica essa transição.
