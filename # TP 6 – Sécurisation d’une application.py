# TP 6 – Sécurisation d’une application

while True:
    try:
        a = float(input("Entrez le numérateur : "))
        b = float(input("Entrez le dénominateur : "))
        resultat = a / b
        print(f"Résultat de la division : {resultat}")
        break
    except ZeroDivisionError:
        print("Erreur : Division par zéro impossible.")
    except ValueError:
        print("Erreur : Veuillez entrer un nombre valide.")
    finally:
        print("--- Fin d'expérience---")
