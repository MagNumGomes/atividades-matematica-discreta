# -*- coding: utf-8 -*-
# Tabelas-verdade
# 1) ¬(p ∨ ¬q)
# 2) (p → q) → p ∧ q
# 3) p ∧ q → (p ↔ q ∨ r)
# Em Python: not = ¬, and = ∧, or = ∨, (not p or q) = →, (p == q) = ↔

import sys
sys.stdout.reconfigure(encoding="utf-8")


def letra(x):
    return "V" if x else "F"


print("=== Tabelas-verdade ===\n")

print("1) ¬(p ∨ ¬q)")
print(" p  q  | ¬(p ∨ ¬q)")
for p in [True, False]:
    for q in [True, False]:
        resultado = not (p or not q)
        print(" " + letra(p) + "  " + letra(q) + "  |     " + letra(resultado))
print()

print("2) (p → q) → p ∧ q")
print(" p  q  | p → q | p ∧ q | (p → q) → p ∧ q")
for p in [True, False]:
    for q in [True, False]:
        implica = (not p) or q
        conjuncao = p and q
        resultado = (not implica) or conjuncao
        print(" " + letra(p) + "  " + letra(q) + "  |   " + letra(implica) +
              "   |   " + letra(conjuncao) + "   |        " + letra(resultado))
print()

print("3) p ∧ q → (p ↔ q ∨ r)")
print(" p  q  r  | p ∧ q | q ∨ r | p ↔ (q ∨ r) | resultado")
for p in [True, False]:
    for q in [True, False]:
        for r in [True, False]:
            conjuncao = p and q
            disjuncao = q or r
            bicondicional = (p == disjuncao)
            resultado = (not conjuncao) or bicondicional
            print(" " + letra(p) + "  " + letra(q) + "  " + letra(r) +
                  "  |   " + letra(conjuncao) + "   |   " + letra(disjuncao) +
                  "   |      " + letra(bicondicional) + "      |     " + letra(resultado))
print()
print("A formula 3 deu V em todas as linhas: e uma tautologia.")
print("As formulas 1 e 2 tem V e F: sao contingencias.")
