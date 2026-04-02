#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage : $0 fichier_utilisateurs.txt"
    exit 1
fi

FICHIER="$1"

if [ ! -f "$FICHIER" ]; then
    echo "Le fichier n'existe pas."
    exit 1
fi

while read -r utilisateur
do
    
    if [ -n "$utilisateur" ]; then
        echo "Création de l'utilisateur : $utilisateur"

        useradd -m "$utilisateur"

        echo "$utilisateur:Temp1234" | chpasswd

        passwd -e "$utilisateur"

        echo "Utilisateur $utilisateur créé avec succès."
    fi
done < "$FICHIER"

echo "Traitement terminé."
