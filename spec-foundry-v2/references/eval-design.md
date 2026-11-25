# Eval design — v2

## Princípio

Um caso de eval é uma **promessa de execução**. Se não há comando que o rode e saída que o comprove, ele não é cobertura — é texto.

## Três camadas

| Camada | O que prova | Como executa | Falha quando |
| --- | --- | --- | --- |
| `target_system` | o sistema faz o que o requisito diz | pytest em node ids reais | teste falha ou não é coletado |
| `contract` | a interface publicada é a interface exercitada | introspecção do app (OpenAPI/schema) | rota/versão/campo ausente |
| `static` | o artefato normativo existe e diz o que deveria | leitura de arquivo | arquivo ausente ou trecho faltando |

Camadas `generator` e `package` da v1 continuam válidas para julgar o **pacote** (qualidade de spec, fidelidade a fonte). Elas não substituem `target_system`: validar schema nunca prova comportamento.

## Anatomia de um caso

```json
{
  "id": "EVAL-008",
  "req": "REQ-008",
  "layer": "target_system",
  "title": "Quatro olhos em resultado crítico",
  "given": "resultado crítico lançado por Ana",
  "when": "Ana confere, Bruno confere e Ana tenta liberar",
  "then": "Ana é bloqueada; Bruno é aceito",
  "node_ids": [
    "tests/test_result.py::test_critico_exige_quatro_olhos_na_conferencia",
    "tests/test_result.py::test_critico_aceita_conferencia_por_outra_pessoa"
  ]
}
```

`given/when/then` existe para revisão humana; `node_ids` existe para execução. Um caso sem os dois é meio caso.

## Cobertura mínima por requisito

| Tipo de requisito | Casos mínimos |
| --- | --- |
| Invariante de domínio (P0) | caminho feliz + violação + fronteira |
| Regra de estado | transição válida + transição inválida |
| Regra de autorização | ator permitido + ator bloqueado |
| Contrato de interface | formato válido + erro mapeado |
| Requisito de processo/documentação | existência + conteúdo obrigatório |

Um requisito crítico com um único caso positivo não está coberto: está anunciado.

## Oráculo

Prefira oráculo determinístico: asserção sobre retorno, estado persistido ou hash. Use `human` só quando o julgamento é qualitativo (clareza de spec, adequação clínica) e declare isso no caso. `llm_judge` ajuda a triagem, nunca fecha um caso crítico sozinho.

**Oráculo circular** é o vício mais comum: o teste chama a mesma função que calcula o valor esperado. Quebre o círculo com valor fixo, fixture explícita ou cálculo independente.

## Anti-padrões

| Anti-padrão | Por que é ruim | Correção |
| --- | --- | --- |
| `execution_status: "passed"` sem relatório | afirma execução inexistente | rodar `run_evals.py` e referenciar o JSON |
| Caso que só verifica que a função não levanta exceção | não mede propriedade | afirmar sobre valor/estado |
| Fixture `missing` com caminho fictício | quebra o pacote em silêncio | `null` + motivo |
| Um caso gigante cobrindo 6 requisitos | falha não localiza a causa | um caso por requisito |
| Mock que substitui a regra testada | testa o mock | mock na borda, domínio real |

## Relatório

`scripts/run_evals.py` grava `evals/reports/<run_id>.json` + `latest.json` + `latest.md`:

```json
{
  "run_id": "20261124T224057Z",
  "totals": {"cases": 26, "passed": 26, "failed": 0},
  "pytest": "pytest exit=0 em 0.61s",
  "results": [{"id": "EVAL-001", "status": "passed", "details": ["..."]}]
}
```

O relatório é a única fonte legítima de `passed`. Se o arquivo não existe, o status é `not_run`.
