# TP 7 – Modélisation d’un système de gestion des étudiants

class Etudiant:
    def __init__(self, nom, matricule, notes):
        self.nom = nom
        self.matricule = matricule
        self.notes = notes

    def calculer_moyenne(self):
        return sum(self.notes) / len(self.notes)

    def afficher_infos(self):
        moyenne = self.calculer_moyenne()
        return f"Étudiant : {self.nom} | Matricule : {self.matricule} | Moyenne : {moyenne:.2f}"

# Test
etudiant1 = Etudiant("jeanne", "ET001", [12, 8, 19, 15])
print(etudiant1.afficher_infos())
