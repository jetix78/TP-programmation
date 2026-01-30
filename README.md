# TP Python — Année 2025-2026

## Informations étudiant
- **Nom** : DJIBU  
- **Prénom** : MULABA Nahum  
- **Filière** : SICC3  
- **Matière** : Python  
- **Année académique** : 2025-2026  

##  Description
Ce dépôt GitHub contient mes Travaux Pratiques (TP) de Python.  
Chaque TP est rangé dans un dossier dédié.

##  Organisation du dépôt
- Chaque TP est dans un dossier : `TP1`, `TP2`, …, `TP10`
- Les fichiers peuvent inclure : `.txt`, `.csv`, `.py`

---

##  Liste des TP

### TP 1 – Prise en main et structures de base
**Contexte réel** : Création d’un premier script utilisé par un service de scolarité  
**Objectifs** : variables, conditions, boucles  

**Travail demandé** :
- Demander à l’utilisateur son nom et son âge
- Afficher s’il est mineur ou majeur
- Afficher tous les nombres pairs entre 1 et 100

**Compétences visées** :
- `input()`, `print()`
- `if` / `else`
- boucle `for`

---

### TP 2 – Fonctions et modularité
**Contexte réel** : Automatisation du calcul des moyennes d’une classe  
**Objectifs** : définir et utiliser des fonctions  

**Travail demandé** :
- Créer une fonction `calcul_moyenne(liste_notes)`
- Créer une fonction `mention(moyenne)` qui retourne : Ajourné, Passable, Bien, Très bien
- Tester avec plusieurs listes de notes

**Compétences visées** :
- `def`
- paramètres et valeurs de retour

---

### TP 3 – Listes, tuples et dictionnaires
**Contexte réel** : Gestion simplifiée des résultats académiques  
**Objectifs** : structures de données  

**Travail demandé** :
- Stocker une liste d’étudiants (nom, âge, moyenne)
- Afficher les étudiants admis (moyenne ≥ 10)
- Calculer la moyenne générale de la classe

**Compétences visées** :
- listes
- dictionnaires
- parcours de collections

---

### TP 4 – Manipulation de chaînes de caractères
**Contexte réel** : Analyse de commentaires saisis par des utilisateurs  
**Objectifs** : traitement de texte  

**Travail demandé** :
- Demander une phrase à l’utilisateur
- Compter le nombre de mots
- Trouver le mot le plus long
- Vérifier si la phrase est un palindrome

**Compétences visées** :
- méthodes sur les chaînes
- découpage et analyse

---

### TP 5 – Fichiers (lecture et écriture)
**Contexte réel** : Sauvegarde et exploitation de données scolaires  
**Objectifs** : persistance des données  

**Travail demandé** :
- Créer un fichier `notes.txt` contenant des notes
- Lire le fichier et calculer la moyenne
- Écrire le résultat dans un fichier `resultat.txt`

**Compétences visées** :
- `open()`
- modes `r`, `w`, `a`

---

### TP 6 – Gestion des exceptions
**Contexte réel** : Sécurisation d’une application utilisée par des non-informaticiens  
**Objectifs** : robustesse des programmes  

**Travail demandé** :
- Créer un programme de division
- Gérer les erreurs : division par zéro, saisie invalide
- Afficher des messages personnalisés

**Compétences visées** :
- `try` / `except` / `finally`

---

### TP 7 – Programmation Orientée Objet (POO)
**Contexte réel** : Modélisation d’un système de gestion des étudiants  
**Objectifs** : classes et objets  

**Travail demandé** :
- Créer une classe `Etudiant`
- Attributs : nom, matricule, notes
- Méthodes : calculer la moyenne, afficher les informations

**Compétences visées** :
- `class`
- `__init__`
- méthodes

---

### TP 8 – Algorithmes et complexité
**Contexte réel** : Optimisation d’un programme utilisé à grande échelle  
**Objectifs** : raisonnement algorithmique  

**Travail demandé** :
- Implémenter le tri à bulles
- Implémenter la recherche linéaire
- Comparer le temps d’exécution avec les fonctions Python

**Compétences visées** :
- algorithmes
- complexité

---

### TP 9 – Manipulation de données (CSV)
**Contexte réel** : Analyse de données RH d’une entreprise  
**Objectifs** : traitement de données  

**Travail demandé** :
- Lire un fichier CSV d’employés
- Calculer le salaire moyen par département
- Générer un rapport textuel

**Compétences visées** :
- module `csv`
- structuration des données

---

### TP 10 – Mini-projet de synthèse
**Contexte réel** : Développement d’une application utile à une organisation réelle  
**Objectifs** : intégration des acquis  

**Travail demandé** :
Développer une application Python permettant de :
- gérer des étudiants
- enregistrer les données dans un fichier
- afficher des statistiques
- utiliser la POO

**Livrables** :
- code source
- rapport explicatif

---

##  Exécution
Pour exécuter un TP, naviguez dans le dossier correspondant et lancez :
```bash
python nom_du_fichier.py
