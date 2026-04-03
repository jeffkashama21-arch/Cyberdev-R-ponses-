1. Navigation et structure Linux

Q/ Expliquez brièvement chaque commande utilisée.

R=> Création d'arborescence 
    Commandes utilisées :

              

1. mkdir : commande qui permet la création d'un dossier . Donc pour la création de
           nos dossiers de l' arborescence on va utiliser cette commande.

                              mkdir projet-linux

2. cd : on utilise cette commande pour accéder dans le dossier <<projet-linux>>
        car c'est la commande qui nous permet de naviguer dans un dossier.

                                 cd projet-linux

3. Étant dans le dossier <<projet-linux>> on va encore utiliser mkdir pour créer les
   autres dossiers de l' arborescence

                       mkdir scripts_logs_sauvergardes_utilisateurs

4. cd : on utilise encore cette commande pour accéder au dossier <<logs>> créé
         dans le dossier <<projet-linux>>

                                        cd logs

5. touch : après avoir accéder dans le dossier <<logs>>, on utilise cette commande
           Pour créer nos 3 fichiers. Car c'est la commande qui permet la création d'un                   fichier.

                           touch fichier1.txt_fichier2.txt_fichier3.txt

6. cd ../ scripts : ensuite nous avons utilisé cette commande pour quitter le dossier
                    <<logs>> pour aller directement dans le dossier <<scripts>>.

7. touch : une fois dans le dossier <<scripts>>, nous avons aussi utilisé cette
           commande pour créer 2 fichiers.

                                   touch fichier1.txt_fichier2.txt

8. pwd : enfin, nous avons utilisé cette commande pour afficher toute
         l'arborescence .
        
 NB : Q\ questions et R => : réponses   
______________________________________________________________________________________________


2. Gestion des permissions

Q\ Expliquez la signification du mode de permission utilisé.

R=> Commande utilisée :

   1. touch :  pour  créer le fichier <<deploy.sh>>
   
                             touch deploy.sh
  
   2. chmod  750  : une fois le fichier  <<deploy.sh>> créé, nous avons utilisé cette commande                     pour lui donner le droit de permission de lecture, d' écriture et d'                           exécution pour le propriétaire; pour lui donner le droit de permission de                      lecture et d' exécution pour le groupe et enfin pour lui retirer tous les                      droits de permission aux autres utilisateurs. 

                            chmod  750  deploy.sh

   En utilisant le chiffre, le 7 va donner le droit de permission rwx au propriétaire; le 5 va    donner le droit de permission r-x au groupe et le 0 va retirer tous les droits aux autres      utilisateurs du fichier.






















