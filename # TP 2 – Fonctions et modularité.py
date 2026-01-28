# TP 2 – Fonctions et modularité

def calcul_moyenne(liste_notes):
    return sum(liste_notes) / len(liste_notes)

def mention(moyenne):
    if moyenne < 10:
        return "Ajourné"
    elif moyenne < 12:
        return "Passable"
    elif moyenne < 14:
        return "Bien"
    elif moyenne < 16:
        return "Très bien"
    else:
        return "Excellent"

# Tests
notes1 = [12, 19, 8, 16]
notes2 = [10, 15, 10, 10]
notes3 = [8, 11, 7, 9]

for notes in [notes1, notes2, notes3]:
    moy = calcul_moyenne(notes)
    print(f"Notes : {notes} -> Moyenne : {moy:.2f} -> Mention : {mention(moy)}")
