# TP 1 – Variables, conditions, boucles

# 1. saisissez votre nom et age
nom = input("Entrez votre nom : ")
age = int(input("Entrez votre âge : "))

# 2. Afficher mineur/majeur
if age < 18:
    print(f"{nom}, vous êtes mineur.")
else:
    print(f"{nom}, vous êtes majeur.")

# 3. Afficher tous les nombres pairs entre 1 et 100
print("Nombres pairs entre 1 et 100 :")
for i in range(1, 101):
    if i % 2 == 0:
        print(i, end=" ")
print()  # pour sauter une ligne
