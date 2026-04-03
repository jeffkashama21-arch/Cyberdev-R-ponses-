
import os

dossier = input("Entrez le chemin du dossier : ")

if not os.path.isdir(dossier):
    print("Le dossier n'existe pas.")
    exit()

fichiers = []
taille_totale = 0

print("\nListe des fichiers :")

for element in os.listdir(dossier):
    chemin = os.path.join(dossier, element)
    
    if os.path.isfile(chemin):
        taille = os.path.getsize(chemin)
        fichiers.append((element, taille))
        
        print(f"{element} : {taille} octets")
        
        taille_totale += taille

if fichiers:
    plus_gros = max(fichiers, key=lambda x: x[1])
    print(f"\nPlus gros fichier : {plus_gros[0]} ({plus_gros[1]} octets)")
else:
    print("Aucun fichier trouvé.")

print(f"Taille totale du dossier : {taille_totale} octets")
