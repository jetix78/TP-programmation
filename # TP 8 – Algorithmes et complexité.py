# TP 8 – Algorithmes et complexité
import time

def tri_bulles(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]

def recherche_lineaire(liste, valeur):
    for i in range(len(liste)):
        if liste[i] == valeur:
            return i
    return -1

# Test
liste_test = [64, 34, 25, 12, 40, 11, 90]
copie = liste_test.copy()

# Tri à bulles
start = time.time()
tri_bulles(liste_test)
temps_bulles = time.time() - start

# Tri Python
start = time.time()
copie.sort()
temps_python = time.time() - start

print(f"Tri à bulles : {liste_test}")
print(f"Tri Python : {copie}")
print(f"Temps bulles : {temps_bulles:.6f}s")
print(f"Temps Python : {temps_python:.6f}s")

# Recherche
print(f"Recherche de 40 : index {recherche_lineaire(liste_test, 40)}")
