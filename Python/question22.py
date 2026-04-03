
import ipaddress

ips = []

for i in range(5):
    ip = input(f"Entrez l'adresse IP {i+1} : ")
    ips.append(ip)

with open("ip_valides.txt", "w") as fichier:

    for ip in ips:
        try:
            
            ipaddress.ip_address(ip)

            print(f"{ip} : valide")

            fichier.write(ip + "\n")

        except ValueError:
            
            print(f"{ip} : invalide")
            