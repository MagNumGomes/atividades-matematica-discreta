# -*- coding: utf-8 -*-
# Exercicio 3.2
# S = { p, q, r, s, t, u, v, w }, A = { p, q, r, s }, B = { r, t, v }, C = { p, s, t, u }
# ~X = complemento (S - X), X + Y = diferenca simetrica, X × Y = produto cartesiano

import sys
sys.stdout.reconfigure(encoding="utf-8")

S = {"p", "q", "r", "s", "t", "u", "v", "w"}
A = {"p", "q", "r", "s"}
B = {"r", "t", "v"}
C = {"p", "s", "t", "u"}

print("=== Exercicio 3.2 ===\n")

print("a) B ∩ C        =", sorted(B & C))
print("b) A ∪ C        =", sorted(A | C))
print("c) ~C           =", sorted(S - C))
print("d) A ∩ B ∩ C    =", sorted(A & B & C))
print("e) B - C        =", sorted(B - C))
print("f) ~(A ∪ B)     =", sorted(S - (A | B)))

AxB = []
for a in sorted(A):
    for b in sorted(B):
        AxB.append((a, b))
print("g) A × B        =", AxB)
print("   quantidade de pares:", len(AxB))

print("h) (A ∪ B) ∩ ~C =", sorted((A | B) & (S - C)))
print("i) A + B        =", sorted(A ^ B))
print("j) B + B        =", sorted(B ^ B))
