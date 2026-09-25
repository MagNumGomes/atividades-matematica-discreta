# -*- coding: utf-8 -*-
# Exercicio 3.1 - transitividade da continencia: se A ⊆ B e B ⊆ C, entao A ⊆ C.
# Pergunta: como fica a demonstracao se A for vazio?
# Resposta: a demonstracao continua valendo. Ela testa "todo a ∈ A esta em C";
# se A e vazio, nao existe nenhum a para testar, entao nao ha contraexemplo
# possivel e a afirmacao e verdadeira por vacuidade. Ou seja, ∅ ⊆ C sempre.

import sys
sys.stdout.reconfigure(encoding="utf-8")


def contido(X, Y):
    for a in X:
        if a not in Y:
            return False
    return True


def testar(A, B, C):
    print("A =", sorted(A), " B =", sorted(B), " C =", sorted(C))
    print("  A ⊆ B ?", contido(A, B))
    print("  B ⊆ C ?", contido(B, C))
    print("  A ⊆ C ?", contido(A, C))
    print()


print("=== Exercicio 3.1 ===\n")

print("A nao vazio:")
testar({1, 2}, {1, 2, 3}, {1, 2, 3, 4})

print("A vazio (caso do exercicio):")
testar(set(), {1, 2, 3}, {1, 2, 3, 4})

print("Com A vazio o laco de contido() nao roda nenhuma vez,")
print("entao a funcao devolve True: ∅ esta contido em qualquer conjunto.")
