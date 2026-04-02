#!/bin/bash

fichier="rapport_systeme.txt"

echo "===== RAPPORT SYSTEME =====" > "$fichier"

echo "Nom de la machine : $(hostname)" >> "$fichier"

echo "Noyau Linux : $(uname -r)" >> "$fichier"

echo "Adresse IP : $(hostname -I | awk '{print $1}')" >> "$fichier"

echo "----- Espace disque -----" >> "$fichier"
df -h >> "$fichier"

echo "----- Utilisation mémoire -----" >> "$fichier"
free -h >> "$fichier"

echo "----- Utilisateurs connectés -----" >> "$fichier"
who >> "$fichier"

echo "Rapport généré dans $fichier"