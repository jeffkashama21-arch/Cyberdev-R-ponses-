
import csv

with open("etudiants.csv", newline='', encoding="utf-8") as fichier:
    lecteur = csv.reader(fichier)
    

    etudiants = []
    next(lecteur)  # ignorer l'en-tête (nom,note)
    
    for ligne in lecteur:
        nom = ligne[0]
        note = float(ligne[1])
        etudiants.append((nom, note))


print("Liste des étudiants :")
for nom, note in etudiants:
    print(f"{nom} : {note}")

total = sum(note for _, note in etudiants)
moyenne = total / len(etudiants)
print("\nMoyenne générale :", moyenne)

meilleur = max(etudiants, key=lambda x: x[1])
print("\nMeilleur étudiant :", meilleur[0], "avec", meilleur[1])

print("\nÉtudiants ayant une note < 10 :")
for nom, note in etudiants:
    if note < 10:
        print(f"{nom} : {note}")