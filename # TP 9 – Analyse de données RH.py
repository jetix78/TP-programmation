# TP 9 – Analyse de données RH
import csv

# Création d'un fichier CSV exemple
donnees = [
    ["Nom", "Département", "Salaire"],
    ["koffi", "IT", 1800],
    ["jean", "RH", 6855],
    ["Claire", "IT", 4700],
    ["victor", "Marketing", 1080],
    ["Ella", "RH", 15000]
]

with open("employes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(donnees)

# Lecture et analyse
salaire_par_dep = {}
with open("employes.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # sauter l'en-tête
    for row in reader:
        nom, departement, salaire = row
        salaire = int(salaire)
        if departement not in salaire_par_dep:
            salaire_par_dep[departement] = []
        salaire_par_dep[departement].append(salaire)

# Calcul des moyennes
print("Salaire moyen par département :")
for dep, salaires in salaire_par_dep.items():
    moyenne = sum(salaires) / len(salaires)
    print(f"{dep} : {moyenne:.2f} $")

# Génération du rapport
with open("rapport_salaires.txt", "w", encoding="utf-8") as f:
    f.write("=== Rapport Salaires ===\n")
    for dep, salaires in salaire_par_dep.items():
        moyenne = sum(salaires) / len(salaires)
        f.write(f"{dep} : {moyenne:.2f} $ ({len(salaires)} employés)\n")
