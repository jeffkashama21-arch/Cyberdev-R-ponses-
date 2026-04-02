#!/bin/bash

echo "Entrez le nom du fichier :"
read fichier

if [ -e "$fichier" ]; then
    echo "Le fichier existe."

    taille=$(stat -c%s "$fichier")
    echo "Taille : $taille octets"

    permissions=$(stat -c%A "$fichier")
    echo "Permissions : $permissions"
else
    echo "Le fichier n'existe pas."
fi
