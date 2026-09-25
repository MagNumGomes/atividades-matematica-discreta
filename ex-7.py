# -*- coding: utf-8 -*-
# Tabela verdade de P ∧ (Q ∨ R) e (P ∧ Q) → R
# As 8 linhas seguem a mesma ordem de P, Q e R que aparece no enunciado.
# Em Python: and = ∧, or = ∨, (not x or y) = →

import sys
sys.stdout.reconfigure(encoding="utf-8")

linhas = [
    (True,  True,  True),
    (False, True,  True),
    (True,  False, True),
    (False, False, True),
    (True,  True,  False),
    (False, True,  False),
    (True,  False, False),
    (False, False, False),
]


def letra(x):
    return "V" if x else "F"


print("=== Tabela verdade: P ∧ (Q ∨ R) e (P ∧ Q) → R ===\n")
print("   | P | Q | R | Q ∨ R | P ∧ Q | P ∧ (Q ∨ R) | (P ∧ Q) → R")
print("---+---+---+---+-------+-------+-------------+------------")

numero = 1
for P, Q, R in linhas:
    disjuncao = Q or R
    conjuncao = P and Q
    primeira = P and disjuncao
    segunda = (not conjuncao) or R
    print(" " + str(numero) + " | " + letra(P) + " | " + letra(Q) + " | " + letra(R) + " |   " + letra(disjuncao) + "   |   " + letra(conjuncao) + "   |      " + letra(primeira) + "      |      " + letra(segunda))
    numero = numero + 1
