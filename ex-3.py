# -*- coding: utf-8 -*-
# Exercicio 3.3
# S = { 0, 1, ..., 9 }, A = { 2, 4, 5, 6, 8 }, B = { 1, 4, 5, 9 }
# C = { x | x ∈ Z ∧ 2 ≤ x < 5 } = { 2, 3, 4 }
# ~X = complemento (S - X), X + Y = diferenca simetrica, X × Y = produto cartesiano

import sys
sys.stdout.reconfigure(encoding="utf-8")

S = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
A = {2, 4, 5, 6, 8}
B = {1, 4, 5, 9}
C = {2, 3, 4}

print("=== Exercicio 3.3 ===\n")

print("a) A ∪ B              =", sorted(A | B))
print("b) A ∩ B              =", sorted(A & B))
print("c) A ∩ C              =", sorted(A & C))
print("d) B ∪ C              =", sorted(B | C))
print("e) A - B              =", sorted(A - B))
print("f) ~A                 =", sorted(S - A))
print("g) A ∩ ~A             =", sorted(A & (S - A)))
print("h) ~(A ∩ B)           =", sorted(S - (A & B)))
print("i) C - B              =", sorted(C - B))
print("j) (C ∩ B) ∪ ~A       =", sorted((C & B) | (S - A)))
print("k) ~(B - A) ∩ (A - B) =", sorted((S - (B - A)) & (A - B)))
print("l) ~(~C ∪ B)          =", sorted(S - ((S - C) | B)))

BxC = []
for b in sorted(B):
    for c in sorted(C):
        BxC.append((b, c))
print("m) B × C              =", BxC)

AxB = []
for a in sorted(A):
    for b in sorted(B):
        AxB.append((a, b))

AxBxC = []
for par in AxB:
    for c in sorted(C):
        AxBxC.append((par, c))
print("n) (A × B) × C        =", len(AxBxC), "pares no formato ((a, b), c)")
print("   os 4 primeiros:", AxBxC[:4])

print("o) B + C              =", sorted(B ^ C))
print("p) (A + B) + C        =", sorted((A ^ B) ^ C))
print("q) (B + B) + B        =", sorted((B ^ B) ^ B))
