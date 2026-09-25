# -*- coding: utf-8 -*-
# Classificacao de relacoes
# A = { a, e, i, o, u }, B = { 1, 2, 3, 4 }, C = { 0, 2, 4, 6 }
# equivalencia = reflexiva + simetrica + transitiva
# ordem parcial = reflexiva + antissimetrica + transitiva

import sys
sys.stdout.reconfigure(encoding="utf-8")

A = ["a", "e", "i", "o", "u"]
B = [1, 2, 3, 4]
C = [0, 2, 4, 6]


def reflexiva(R, X):
    for x in X:
        if (x, x) not in R:
            return False
    return True


def simetrica(R):
    for x, y in R:
        if (y, x) not in R:
            return False
    return True


def antissimetrica(R):
    for x, y in R:
        if (y, x) in R and x != y:
            return False
    return True


def transitiva(R):
    for x, y in R:
        for w, z in R:
            if y == w and (x, z) not in R:
                return False
    return True


def classificar(titulo, R, X):
    print(titulo)
    print("   pares:", R)
    ref = reflexiva(R, X)
    sim = simetrica(R)
    ant = antissimetrica(R)
    tra = transitiva(R)
    print("   reflexiva:", ref, " simetrica:", sim,
          " antissimetrica:", ant, " transitiva:", tra)
    if ref and sim and tra:
        print("   => relacao de equivalencia")
    elif ref and ant and tra:
        print("   => relacao de ordem parcial")
    else:
        print("   => nao e equivalencia nem ordem parcial")
    print()


print("=== Classificacao de relacoes ===\n")

# 1) relacao dada no enunciado
classificar("1) R: A → A", [("a", "a"), ("a", "e"), ("e", "i"), ("o", "u")], A)

# 2) =: C → C
igual = []
for x in C:
    for y in C:
        if x == y:
            igual.append((x, y))
classificar("2) =: C → C", igual, C)

# 3) ≤: B → B
menor_igual = []
for x in B:
    for y in B:
        if x <= y:
            menor_igual.append((x, y))
classificar("3) ≤: B → B", menor_igual, B)

# 4 e 5 vao de um conjunto para outro diferente, entao reflexiva/simetrica/
# transitiva nao se aplicam (nao existe o par invertido <y, x>).
print("4) φ: A → C")
print("   pares: []  (relacao vazia, nao relaciona nenhum elemento)")
print("   reflexiva/simetrica/transitiva nao se aplicam: A e C sao conjuntos diferentes")
print()

BxC = []
for x in B:
    for y in C:
        BxC.append((x, y))
print("5) B × C")
print("   pares:", BxC)
print("   e o produto cartesiano inteiro: relacao total de B para C")
print("   reflexiva/simetrica/transitiva nao se aplicam: B e C sao conjuntos diferentes")
