from datetime import datetime

mot_de_passe_correct = "Secret123"

tentatives_max = 3

fichier_log = open("access.log", "a")

for i in range(tentatives_max):
    mot_de_passe = input("Entrez le mot de passe : ")

    maintenant = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if mot_de_passe == mot_de_passe_correct:
        print("Accès autorisé")
        fichier_log.write(f"{maintenant} - SUCCES\n")
        break
    else:
        print("Accès refusé")
        fichier_log.write(f"{maintenant} - ECHEC\n")

        if i == tentatives_max - 1:
            print("Nombre de tentatives dépassé.")

fichier_log.close()