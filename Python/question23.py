import re
from collections import Counter

fichier = "server.log"

nb_failed = 0
ips = []

pattern_ip = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"

with open(fichier, "r", encoding="utf-8") as f:
    for ligne in f:
        
        if "failed login" in ligne.lower():
            nb_failed += 1
        
        trouvees = re.findall(pattern_ip, ligne)
        ips.extend(trouvees)

if ips:
    compteur = Counter(ips)
    ip_plus_frequente, nb = compteur.most_common(1)[0]
else:
    ip_plus_frequente, nb = None, 0

print("Nombre de 'failed login' :", nb_failed)
print("Nombre total d'IP trouvées :", len(ips))

if ip_plus_frequente:
    print("IP la plus fréquente :", ip_plus_frequente, "(", nb, "fois )")
else:
    print("Aucune IP trouvée.")

print("\n===== RÉSUMÉ =====")
print(f"Tentatives échouées : {nb_failed}")
print(f"Total IP extraites : {len(ips)}")

if ip_plus_frequente:
    print(f"IP la plus active : {ip_plus_frequente} ({nb} fois)")
    