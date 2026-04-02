#!/bin/bash

echo "Entrez le chemin du dossier à sauvegarder :"
read dossier

if [ ! -d "$dossier" ]; then
    echo "Le dossier n'existe pas."
    exit 1
fi

mkdir -p sauvegardes
date_jour=$(date +%F)

nom_archive="sauvegardes/backup_$date_jour.tar.gz"
tar -czf "$nom_archive" "$dossier"

echo "Sauvegarde réalisée : $nom_archive"