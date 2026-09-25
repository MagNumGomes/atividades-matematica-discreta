# -*- coding: utf-8 -*-
# Relacoes, matriz e grafo
# A = { 0, 1, 2, 3 }, B = { 2, 3, 5, 6 }, C = { 2, 4, 6, 8 }
# A matriz tem 1 onde o par pertence a relacao e 0 onde nao pertence.
# O grafo e mostrado como setas x --> y (par <x, y> da relacao).

import sys
sys.stdout.reconfigure(encoding="utf-8")

A = [0, 1, 2, 3]
B = [2, 3, 5, 6]
C = [2, 4, 6, 8]


def mostrar(titulo, R, X, Y):
    print(titulo)
    print("   pares:", R)

    print("   matriz:")
    print("        ", "  ".join(str(y) for y in Y))
    for x in X:
        linha = []
        for y in Y:
            if (x, y) in R:
                linha.append("1")
            else:
                linha.append("0")
        print("     ", x, "|", "  ".join(linha))

    print("   grafo:")
    for x, y in R:
        print("      ", x, "-->", y)
    print()


print("=== Relacoes, matriz e grafo ===\n")

# a) A × A
AxA = []
for x in A:
    for y in A:
        AxA.append((x, y))
mostrar("a) A × A", AxA, A, A)

# b) A × B
AxB = []
for x in A:
    for y in B:
        AxB.append((x, y))
mostrar("b) A × B", AxB, A, B)

# c) >: A × B
maior = []
for x in A:
    for y in B:
        if x > y:
            maior.append((x, y))
mostrar("c) >: A × B", maior, A, B)

# d) =: C × C
igual_C = []
for x in C:
    for y in C:
        if x == y:
            igual_C.append((x, y))
mostrar("d) =: C × C", igual_C, C, C)

# e) ≤: C × C
menor_igual = []
for x in C:
    for y in C:
        if x <= y:
            menor_igual.append((x, y))
mostrar("e) ≤: C × C", menor_igual, C, C)

# f) relacao dada no enunciado
mostrar("f) R: A → B", [(0, 5), (0, 6), (2, 6)], A, B)

# g) =: B → B
igual_B = []
for x in B:
    for y in B:
        if x == y:
            igual_B.append((x, y))
mostrar("g) =: B → B", igual_B, B, B)

# h) (A, ≥)
maior_igual = []
for x in A:
    for y in A:
        if x >= y:
            maior_igual.append((x, y))
mostrar("h) (A, ≥)", maior_igual, A, A)

# i) relacao dada no enunciado
mostrar("i) R: C → C", [(2, 2), (2, 4), (4, 6), (4, 8), (6, 8)], C, C)

print("Obs.: nos itens b, c e f a relacao vai de A para B (conjuntos diferentes),")
print("entao o grafo e bipartido: uma coluna com os elementos de A e outra com os de B.")
