#!/bin/bash

echo "Entrez le nom du fichier de logs :"
read fichier

if [ ! -f "$fichier" ]; then
    echo "Erreur : le fichier n'existe pas."
    exit 1
fi

total=$(wc -l < "$fichier")

nb_error=$(grep -c "ERROR" "$fichier")

nb_warning=$(grep -c "WARNING" "$fichier")

echo "Nombre total de lignes : $total"
echo "Nombre de lignes contenant ERROR : $nb_error"
echo "Nombre de lignes contenant WARNING : $nb_warning"

echo "Les 3 dernières lignes du fichier :"
tail -n 3 "$fichier"