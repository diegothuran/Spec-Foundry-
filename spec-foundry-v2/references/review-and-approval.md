# Revisão e aprovação

## Três níveis, três evidências

| Nível | Quem | Evidência exigida |
| --- | --- | --- |
| Check estrutural | script | relatório JSON de `validate_package.py` |
| Revisão técnica | humano ou LLM com rubrica | nota por rubrica + arquivo/linha que justifica |
| Aprovação de baseline | humano responsável | mensagem explícita na mesma revisão/escopo |

Nenhum nível substitui o outro. Script aprovando não é revisão; LLM revisando não é aprovação.

## Rubricas (escala 0–2)

| Rubrica | 0 | 2 |
| --- | --- | --- |
| R1 Qualidade de requisito | vago | verificável, com erro e borda |
| R2 Qualidade de eval | declarativo | executável, vinculado, com node ids válidos |
| R3 Auditabilidade | sem autor/registro | hash verificável + versionamento |
| R4 Isolamento | filtro opcional | filtro obrigatório + teste de vazamento |
| R5 Honestidade do limite | sugere pronto | limite com consequência e gatilho |

Média < 1,5 em qualquer rubrica bloqueia promoção para `approved_baseline`.

## Como escrever um achado

```
[REQ-008] spec 03, seção 3: quatro olhos descrito sem citar que a comparação é por
ator declarado. Efeito: leitor assume controle técnico. Correção: adicionar nota de
limite (ASM-004) e referenciar RSK-005.
```

Localizado, com efeito e correção. Achado sem correção proposta é reclamação.

## O que não se faz na revisão

- Reescrever decisão aprovada por preferência estética.
- Apagar requisito que falhou em vez de registrar a falha.
- Promover `not_run` para `passed` porque "o teste provavelmente passaria".
- Aprovar baseline com pergunta bloqueante aberta.

## Registro de aprovação

```json
{"revision": "r001", "scope": "fundacao", "actor": "nome", "decision": "approve",
 "evidence_ref": "SRC-010", "at": "2026-11-24"}
```

O registro é declaração auditável pelo leitor. Não é assinatura digital, não prova identidade e não é ledger imutável. Dizer isso explicitamente é parte da entrega.

## Depois de aprovado

Baseline aprovada é congelada. Mudança entra como `r002` com diff de impacto (`updates-and-isolation.md`). Aprovação nova é necessária; a anterior não se transfere.
