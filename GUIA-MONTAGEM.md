# Montar e usar a skill Spec Foundry no Claude

A skill está organizada para receber ideias e definições em texto, imagens e PDFs e produzir uma fundação de projeto com specs e eval specs. Use o ZIP `spec-foundry-claude.zip` para instalação no Claude. O ZIP `claude-spec-foundry-kit.zip` contém o código-fonte da skill, este guia e os testes para manutenção; **não envie o kit inteiro como se fosse a skill**.

O método não depende de Agno, API própria, banco ou Data Terminal. Essas tecnologias podem ser opções de um sistema-alvo, mas não são necessárias para gerar suas especificações. A leitura multimodal e a pesquisa dependem das ferramentas e permissões da superfície do Claude em uso.

## 1. Arquivos que compõem a skill

```text
spec-foundry/
  SKILL.md
  references/
    intake-and-evidence.md
    discovery-and-scope.md
    model-contract.md
    output-contract.md
    eval-design.md
    review-and-approval.md
    updates-and-isolation.md
    domain-guardrails.md
    examples.md
    tooling.md
  schemas/
    project-model.schema.json
  templates/
    project-model.json
    foundation/
      README.md
      AGENTS.md
      CLAUDE.md
      docs/
        specs/
          01-product-spec.md
          02-requirements.md
          03-system-design.md
          04-implementation-plan.md
          05-agent-configuration.md
        domain-model.md
        data-contracts.md
        traceability.md
        open-questions.md
        assumptions-and-risks.md
        review.md
        change-impact.md
        adr/000-template.md
      evals/
        eval-spec.md
        rubrics.md
  scripts/
    common.py
    init_project.py
    validate_package.py
    bundle_project.py
```

`SKILL.md` tem o nome, a descrição de ativação e o fluxo principal. References contêm regras carregadas conforme a tarefa. Templates são checklists para Claude transformar em documentos do projeto, não especificações prontas. O schema define o modelo canônico. Os scripts apoiam scaffold, verificação e exportação; não chamam LLM nem fazem OCR.

A pasta externa do kit contém `tests/test_skill.py`, `tests/behavior-cases.json`, inputs sintéticos e `tooling/build_model_schema.py`, além da ferramenta de empacotamento. Nada disso precisa virar dependência da skill instalada. Os testes sintéticos são de manutenção, não exemplos automaticamente corretos para o projeto do cliente.

## 2. Instalar no Claude de navegador

Habilite criação/edição de arquivos e execução de código nas capacidades da sua conta. A configuração pode estar sob controle de administradores em uma organização. A documentação atual descreve upload de skills personalizadas em **Customize > Skills** [1].

Escolha adicionar/criar uma skill e depois **Upload a skill**. Envie `spec-foundry-claude.zip` e ative `spec-foundry`. Não extraia e envie só `SKILL.md`: ele depende das referências/templates/scripts do mesmo diretório.

O ZIP da skill contém uma única pasta de raiz `spec-foundry/`, e nela `SKILL.md` e seus recursos. Isso segue a estrutura de pasta documentada para upload [2]. O frontmatter usa `name: spec-foundry` e uma descrição curta do comportamento. A grafia em maiúsculas de `SKILL.md` mantém compatibilidade com o Claude Code.

Faça uma conversa nova e peça explicitamente: “Use a skill spec-foundry para analisar estes materiais e gerar a fundação do projeto”. Verifique se o resultado usa o fluxo e os arquivos esperados. Instalação, ativação e comportamento no Claude ainda precisam ser testados em sua conta; os checks deste kit não substituem esse passo.

Se não aparecer a opção, confirme habilitação/permissões na conta e a documentação do produto, em vez de colar o ZIP em um chat comum e assumir que foi instalado. Usar os arquivos anexados em uma conversa é diferente de instalar uma skill reutilizável.

## 3. Instalar no Claude Code

Extraia o ZIP. Copie a pasta `spec-foundry`, inteira, para **uma** destas opções [3]:

```text
~/.claude/skills/spec-foundry/                 # pessoal, na máquina
<repositorio>/.claude/skills/spec-foundry/     # compartilhada pelo repositório
```

Não mantenha cópias divergentes do mesmo nome em ambos os lugares sem entender a prioridade de carregamento. Não sobrescreva uma instalação editada sem backup. Reinicie/inicie a sessão, confira as skills disponíveis e execute:

```text
/spec-foundry Crie a fundação deste projeto a partir dos arquivos em ./inputs.
Não implemente o sistema. Primeiro consolide o entendimento e as perguntas bloqueantes.
```

Os scripts precisam de Python 3.10+ quando executados. Não têm pacotes Python externos obrigatórios. Permissões de arquivos/shell são da sua sessão; instalar skill não é permissão para ler qualquer pasta, publicar arquivos ou usar credenciais.

## 4. Primeiro uso recomendado

Comece com um projeto pequeno, uma definição textual e um anexo inofensivo. Identifique projeto/pasta e o recorte. Se comparar concorrentes, peça equivalência funcional com identidade própria, não reprodução de código, marca ou conteúdo proprietário.

Prompt inicial sugerido:

```text
Use spec-foundry para criar a fundação do projeto Portal de Documentos.
Público: uma equipe pequena que compartilha documentos com clientes.
Entrada: minha descrição e os anexos desta conversa.
Saída: specs, eval specs e pacote de arquivos para outra IA implementar.
Não construa o produto. Não escolha stack antes de justificar alternativas.
Diferencie definição, hipótese, proposta e decisão aprovada.
Primeiro mostre o entendimento e as poucas perguntas que bloqueiam o recorte.
```

Quando Claude fizer perguntas, responda explicitamente. Não chamar toda resposta de aprovação do pacote inteiro. Uma confirmação de requisito pode apoiar uma decisão localizada; a aprovação de baseline exige revisão e recorte claros.

Para gerar sem resolver tudo:

```text
Gere a fundação da revisão r001 em discovery.
Mantenha abertas as decisões que faltam, mas entregue os documentos completos,
com riscos, tarefas de levantamento/POC e evals futuras como not_run.
Não invente valores para preencher lacunas.
```

Scaffold vazio não conta como essa entrega. O agente deve substituir instruções dos templates por conteúdo concreto, N/A justificado ou pendência explícita.

## 5. Fluxo que a skill deve seguir

Inventariar fontes → extrair conteúdo com locators e limites → registrar claims → consolidar requisitos/questões/conflitos → perguntar o que bloqueia → gerar cinco anchors e documentação complementar → criar eval specs → verificar coerência/contratos → revisar com humano → registrar estado → exportar.

O modelo usa cadeia `SRC → EVD → CLM → REQ → DEC/TASK/RSK/EVAL`. A descrição em Markdown e o JSON precisam concordar. ID existente não é prova de pertinência; revisão semântica compara enunciado, trecho e condição.

Os cinco anchors são produto, requisitos, desenho, plano e configuração de agentes. Essa é a organização usada neste trabalho; não é alegação de certificação por um padrão externo chamado Evan Spec. As eval specs complementam essa estrutura.

Não atribuir à imagem o desenho do backend. Não transformar uma hipótese de IA em regra clínica, jurídica ou contábil. Em domínios sensíveis, exigir fontes atuais e revisão especializada para as decisões materiais.

## 6. Specs, eval specs e resultados são coisas diferentes

Os testes do **gerador** avaliam extração/compreensão/abstenção/mudanças e segurança do fluxo. Os checks do **pacote** validam estruturas, referências, cobertura e coerência. As evals do **sistema-alvo** descrevem testes do produto que outra IA ainda construirá.

Os casos ficam em `evals/cases.json`, espelhando `eval_cases` do modelo. JSON foi escolhido para validar com biblioteca padrão; os critérios, explicações e rubrics permanecem em Markdown. Cada caso tem expected, oracle, severidade, entrada, fixture e executor quando existirem.

`not_run` significa não executado. `blocked` significa pré-requisito ausente. `passed`/`failed` exigem execução, executor e relatório/evidência compatíveis. Fixture sintética não é gold humano e validador local não produz resultado de teste clínico ou funcional do alvo.

Prontidão: `discovery` tem bloqueios relevantes; `ready_for_review` permite revisão; `approved_baseline` exige evidência de revisão humana e aprovação da mesma revisão/escopo. Esta skill registra declarações locais, não identidade autenticada nem trilha imutável. Aprovar spec não significa aprovar release de software.

## 7. Scripts e verificação

O Claude pode usar scripts quando a execução é autorizada. Também é possível rodar localmente. Defina `SKILL_DIR` como a pasta extraída/instalada; não use caminhos do ambiente em que este kit foi criado.

```bash
python3 "$SKILL_DIR/scripts/init_project.py" \
  --name "Portal" --project-id "portal" --scope "POC de documentos privados" \
  --output "./projects/portal/r001"

# Preencher fontes/modelo/docs/cases com o Claude ANTES dos comandos seguintes.
python3 "$SKILL_DIR/scripts/validate_package.py" \
  --project "./projects/portal/r001" --report "./checks/portal-r001.json"

python3 "$SKILL_DIR/scripts/bundle_project.py" \
  --project "./projects/portal/r001" --output "./exports/portal-r001.zip"
```

A primeira etapa só inicializa templates e modelo vazio; falha de validação nesse ponto é esperada. O check local implementa apenas o subconjunto do schema fornecido e invariantes locais. Não usar como validador universal de OpenAPI/JSON Schema do produto.

O exportador gera manifest/hashes e só inclui artefatos registrados. Originais privados em sources ficam de fora. O destinatário pode verificar o pacote extraído com o script incluído e `--exported`; isso checa integridade local e declara que fontes privadas ausentes não foram verificadas. Hash não prova autoria/autenticidade.

Revise dados pessoais/segredos antes do export. O bundler rejeita caminhos inseguros, alguns formatos de credencial e sources, mas não é scanner DLP: um Markdown pode conter dados sensíveis. Não usar o ZIP de projeto como upload da skill.

## 8. Revisar e atualizar projetos

Prompt de revisão:

```text
Use spec-foundry no modo revisão. Compare o pacote com as fontes.
Aponte requisitos sem suporte, decisões implícitas, conflitos,
contratos incoerentes e evals com oracle circular. Não reescreva decisões
aprovadas nem declare aprovação por sucesso de testes estruturais.
```

Prompt de atualização:

```text
Use spec-foundry para criar r002 a partir do pacote r001 e desta nova definição.
Preserve r001 e IDs não alterados. Entregue o impacto em requisitos,
contratos, tarefas e evals. Não reutilize a aprovação de r001 como aprovação de r002.
```

Para retomar em outra conversa, anexe o pacote anterior e fontes autorizadas ou dê acesso à pasta correta. Não presumir que Claude lembra projetos anteriores. Mudar a skill não migra todos os modelos automaticamente: este schema 1.0 é perfil próprio da skill, diferente da fundação anterior do SaaS Spec Foundry.

## 9. Manter e testar a skill

Edite `SKILL.md` quando mudar fluxo/ativação; referências quando mudar método; templates quando mudar formato; schema e validadores em conjunto quando mudar contrato. Atualize versão declarada no exportador/guia e regenere o ZIP. Faça testes locais e comportamentais antes de substituir instalação existente.

No diretório do kit:

```bash
python3 tooling/build_model_schema.py
python3 -m unittest discover -s tests -v
python3 tooling/package_kit.py --output-dir ./dist
```

O builder materializa o schema e modelo vazio a partir do contrato versionado. Não precisa rodar em cada projeto. `tests/test_skill.py` testa o código local com fixtures sintéticas. `tests/behavior-cases.json` contém testes do comportamento do Claude ainda não executados; siga os inputs/gabaritos e não use apenas a saída gerada como gabarito.

O protocolo inclui texto, conflito, injeção de instrução, revisão e leitura multimodal com ferramentas indisponíveis. PDFs/imagens de teste precisam de exemplos inofensivos anotados por humano; os arquivos reais dessas modalidades ainda são pré-requisitos a preparar. Nunca marcar pass só porque um PDF foi anexado.

A validação do formato, sintaxe, schemas, testes locais e integridade ZIP pode ser feita fora do Claude. Carregamento, qualidade multimodal e resultados reais do uso precisam ser testados na sua conta. Não afirmar instalação concluída ou performance do agente sem esse teste.

## 10. Evolução opcional

Quando a skill estiver útil, um plugin pode empacotar comandos/skills adicionais e componentes suportados em cada superfície. Esta entrega é uma skill independente, sem plugin ou MCP configurado. Primeiro validar o método em projetos pequenos; portal multiusuário, jobs persistentes e aprovação autenticada só entram se houver necessidade de aplicação própria.

## References

[1]: https://support.claude.com/en/articles/12512180-use-skills-in-claude "Claude — ativar e enviar skills personalizadas"
[2]: https://support.claude.com/en/articles/12512198-creating-custom-skills "Claude — estrutura e ZIP de uma skill personalizada"
[3]: https://code.claude.com/docs/en/skills "Claude Code — skills locais e por repositório"

Fontes consultadas em 04/11/2026. Autor: Manus AI. Versão do kit: 1.0.0.
