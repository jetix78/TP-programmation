# TP 10 – Application de gestion d'étudiants

import json
from datetime import datetime

class Etudiant:
    def __init__(self, nom, matricule, notes):
        self.nom = nom
        self.matricule = matricule
        self.notes = notes

    def moyenne(self):
        return sum(self.notes) / len(self.notes)

    def mention(self):
        moy = self.moyenne()
        if moy < 10:
            return "Ajourné"
        elif moy < 12:
            return "Passable"
        elif moy < 14:
            return "Bien"
        elif moy < 16:
            return "Très bien"
        else:
            return "Excellent"

    def to_dict(self):
        return {
            "nom": self.nom,
            "matricule": self.matricule,
            "notes": self.notes
        }

class GestionEtudiants:
    def __init__(self, fichier="etudiants.json"):
        self.fichier = fichier
        self.etudiants = self.charger()

    def ajouter(self, etudiant):
        self.etudiants.append(etudiant)
        self.sauvegarder()

    def sauvegarder(self):
        with open(self.fichier, "w", encoding="utf-8") as f:
            json.dump([e.to_dict() for e in self.etudiants], f, indent=4)

    def charger(self):
        try:
            with open(self.fichier, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Etudiant(e["nom"], e["matricule"], e["notes"]) for e in data]
        except FileNotFoundError:
            return []

    def statistiques(self):
        if not self.etudiants:
            return "Aucun étudiant enregistré."

        moyennes = [e.moyenne() for e in self.etudiants]
        admis = [e for e in self.etudiants if e.moyenne() >= 10]

        return {
            "total": len(self.etudiants),
            "admis": len(admis),
            "ajournes": len(self.etudiants) - len(admis),
            "moyenne_generale": sum(moyennes) / len(moyennes) if moyennes else 0
        }

    def afficher_tous(self):
        for etudiant in self.etudiants:
            print(f"{etudiant.nom} ({etudiant.matricule}) - Moyenne : {etudiant.moyenne():.2f} - Mention : {etudiant.mention()}")

# Menu principal
def main():
    gestion = GestionEtudiants()

    while True:
        print("\n=== Gestion des Étudiants ===")
        print("1. Ajouter un étudiant")
        print("2. Afficher tous les étudiants")
        print("3. Voir les statistiques")
        print("4. Quitter")
        choix = input("Choix : ")

        if choix == "1":
            nom = input("Nom : ")
            matricule = input("Matricule : ")
            notes_str = input("Notes (séparées par des espaces) : ")
            notes = list(map(float, notes_str.split()))
            etudiant = Etudiant(nom, matricule, notes)
            gestion.ajouter(etudiant)
            print("Étudiant ajouté.")

        elif choix == "2":
            gestion.afficher_tous()

        elif choix == "3":
            stats = gestion.statistiques()
            if isinstance(stats, dict):
                print(f"Total étudiants : {stats['total']}")
                print(f"Admis : {stats['admis']}")
                print(f"Ajournés : {stats['ajournes']}")
                print(f"Moyenne générale : {stats['moyenne_generale']:.2f}")
            else:
                print(stats)

        elif choix == "4":
            print("Au revoir !")
            break

if __name__ == "__main__":
    main()
