# TP 3 – Gestion simplifiée des résultats académiques

etudiants = [
    {"nom": "jean", "age": 19, "moyenne": 14},
    {"nom": "tariq", "age": 18, "moyenne": 7},
    {"nom": "koffi", "age": 25, "moyenne": 13},
    {"nom": "jules", "age": 21, "moyenne": 9},
    {"nom": "ella", "age": 20, "moyenne": 18}
]

# 1. Afficher les étudiants admis (moyenne >= 10)
print("Étudiants admis :")
for etudiant in etudiants:
    if etudiant["moyenne"] >= 10:
        print(f"{etudiant['nom']} - Moyenne : {etudiant['moyenne']}")

# 2. Calculer la moyenne générale
moyennes = [etudiant["moyenne"] for etudiant in etudiants]
moyenne_generale = sum(moyennes) / len(moyennes)
print(f"\nMoyenne générale de la classe : {moyenne_generale:.2f}")
