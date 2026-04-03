import re

mot_de_passe = input("Entrez votre mot de passe : ")

erreurs = []

if len(mot_de_passe) < 10:
    erreurs.append("Le mot de passe doit contenir au moins 10 caractères.")

if not re.search(r"[A-Z]", mot_de_passe):
    erreurs.append("Le mot de passe doit contenir au moins une majuscule.")

if not re.search(r"[a-z]", mot_de_passe):
    erreurs.append("Le mot de passe doit contenir au moins une minuscule.")

if not re.search(r"[0-9]", mot_de_passe):
    erreurs.append("Le mot de passe doit contenir au moins un chiffre.")

if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", mot_de_passe):
    erreurs.append("Le mot de passe doit contenir au moins un caractère spécial.")

if not erreurs:
    print("Mot de passe valide ")
else:
    print("Mot de passe invalide")
    print("Problèmes :")
    for erreur in erreurs:
        print("-", erreur)
        