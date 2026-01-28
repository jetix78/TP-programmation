# TP 4 – Analyse de commentaires

# 1. entrer une phrase
phrase = input("Entrez une phrase : ")

# 2. Compter le nombre de mots
mots = phrase.split()
print(f"Nombre de mots : {len(mots)}")

# 3. Trouver le mot le plus long
mot_le_plus_long = max(mots, key=len)
print(f"Mot le plus long : {mot_le_plus_long}")

# 4. Vérifier si la phrase est un palindrome (sans espaces ni majuscules)
phrase_nettoyee = phrase.lower().replace(" ", "").replace(",", "").replace(".", "")
est_palindrome = phrase_nettoyee == phrase_nettoyee[::-1]
print(f"C'est un palindrome : {est_palindrome}")
