# NN — Título da spec

**Requisitos:** REQ-001 · **Casos de eval:** EVAL-001

## 1. Objetivo

O que esta área garante e por que ela existe.

## 2. Regras

| Regra | Condição | Efeito |
| --- | --- | --- |
| A1 | entrada válida | resultado observável |
| A2 | violação | erro tipado (`ValidationError`) |

## 3. Casos de borda

| Cenário | Comportamento esperado |
| --- | --- |
| entrada duplicada | rejeitada com `Conflict` |

## 4. Limite declarado

O que esta spec **não** cobre, com consequência operacional.

## 5. Ganchos de eval

- `tests/test_area.py::test_caminho_feliz` — A1.
- `tests/test_area.py::test_violacao` — A2.
