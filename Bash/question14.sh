#!/bin/bash

utilisation=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')

echo "Utilisation actuelle : $utilisation%"

if [ "$utilisation" -gt 90 ]; then

    echo "CRITIQUE : utilisation supérieure à 90 % !"
elif [ "$utilisation" -gt 80 ]; then

    echo "ALERTE : utilisation supérieure à 80 %."
else
    echo " Tout est normal."
fi