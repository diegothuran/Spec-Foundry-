# Atualizações, revisões e isolamento

## Nova revisão, não sobrescrita

`r001` aprovada não é editada. Mudança gera `r002` com:

1. Cópia do modelo com `release: r002`.
2. Diff de impacto: fonte → requisito → decisão → arquivo → eval → teste.
3. Registro do que foi invalidado (aprovação anterior, eval que deixou de valer).
4. Status `discovery` ou `ready_for_review` conforme gates.

## Diff de impacto

```markdown
| Origem | Mudança | Afetados | Ação |
| SRC-011 (nova norma) | exige retenção de 20 anos | REQ-011, ASM-001 | novo requisito + ADR |
| DEC-003 | revisão de sharding | docs/data-contracts | r002 |
```

Toda linha precisa de ação: incluir, alterar, retirar ou "sem impacto com motivo".

## Preservar IDs

`REQ-*` mantém o ID enquanto a identidade semântica for a mesma. Se o requisito muda de sentido, criar novo ID e marcar o antigo como `superseded` com referência. Renumerar em massa destrói histórico de auditoria.

## Isolamento entre projetos

- Um projeto por pasta de saída; nunca reaproveitar pasta existente sem confirmação.
- Material de cliente não entra em `templates/` nem em `references/examples.md`.
- Exemplo em template é sintético e marcado como sintético.
- Ao retomar projeto, ler arquivos do projeto — nunca confiar em memória de sessão anterior.

## Retomada

Se o pacote anterior não estiver acessível:

1. Pedir o ZIP ou a pasta.
2. Não reconstruir de memória: memória de conversa não é fonte.
3. Se o usuário autorizar reconstrução parcial, marcar tudo que veio de memória como `proposal` com `quality: uncertain`.

## Congelamento

Ao submeter para revisão, congelar revisão + escopo. Mudança durante a revisão invalida o parecer — melhor esperar que aprovar algo que já mudou.
