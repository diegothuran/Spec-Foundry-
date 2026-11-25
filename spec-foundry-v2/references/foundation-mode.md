# Modo fundação — construir o mínimo que prova o domínio

## O que é (e o que não é)

**É:** o menor código que faz os requisitos P0 passarem em teste, com domínio puro, persistência substituível e uma borda HTTP que expõe o contrato.

**Não é:** MVP, produto, UI, autenticação, integração completa. Fundação é a parte que, se estiver errada, contamina tudo depois.

## Ordem de construção

Construir nesta ordem, porque cada passo depende do anterior:

1. **Erros e identificadores** — vocabulário de falha (`ValidationError`, `NotFound`, `Conflict`, `InvalidTransition`, `AuthorizationError`) e IDs opacos prefixados.
2. **Entidades e invariantes** — dataclasses `frozen=True, slots=True`, construção validada, transição como função pura que devolve nova instância.
3. **Persistência** — schema explícito, `tenant_id` em toda tabela, índices de unicidade, verificação de integridade.
4. **Casos de uso** — serviço de aplicação, relógio injetado, auditoria, transação.
5. **Integrações** — parser de protocolo externo (ex.: HL7), isolado e testável sem rede.
6. **Borda** — API, headers, mapeamento de erro de domínio para status HTTP.
7. **Ferramentas** — exportar contrato, rodar evals, checar rastreabilidade.
8. **Docs** — specs, ADRs, riscos, perguntas; só depois que o código estabilizou.

Inverter 2 e 3 é o erro clássico: schema nasce do banco, não do domínio, e a regra passa a morar em SQL.

## Regras de código

- Domínio não importa nada de framework, ORM ou HTTP. Se importar, a regra está no lugar errado.
- Toda função que muda estado devolve nova instância; nada de mutação silenciosa.
- Tempo vem de relógio injetado — nunca `datetime.now()` dentro da regra.
- Erro de domínio é exceção tipada, não string.
- Persistência é porta: trocar SQLite por Postgres não pode tocar no domínio nem nos testes de domínio.
- Hash e assinatura ficam em funções pequenas e documentadas, com o formato canônico escrito em `data-contracts.md`.

## Regra de tamanho

A fundação deve caber em leitura de uma sessão. Se o pacote tem mais de ~2.500 linhas de código de produção, provavelmente virou produto pela metade — corte escopo, não qualidade.

## Testes

- Um arquivo por área de domínio (`test_patient.py`, `test_report.py`).
- Marcador obrigatório: `@pytest.mark.req("REQ-00X")`, registrado em `pytest.ini`/`pyproject.toml`.
- `conftest.py` com fixtures de fluxo completo (`released_order`) e helpers (`build_order`), para que cada teste diga o que testa em três linhas.
- Todo teste tem asserção sobre valor/estado, nunca só "não levantou".
- Pelo menos um teste por invariante negativa (o que o sistema **não** deixa fazer).

## Definition of done da fundação

| Critério | Verificação |
| --- | --- |
| Suíte passa do zero em máquina limpa | `make install && make test` |
| Todo REQ tem teste | `tools/check_traceability.py` |
| Todo caso de eval roda | `tools/run_evals.py` |
| Contrato exportado bate com o servido | eval de camada `contract` |
| CI reproduz os três acima | workflow versionado |
| README diz o que não existe | leitura humana |

## Como declarar limite

No README e nas specs, escrever o limite com consequência, não com lista:

> `X-Tenant-Id` e `X-Actor` não são autenticados: **a API não pode ser exposta à internet neste estado**.

Lista de features ausentes informa; consequência operacional protege.
