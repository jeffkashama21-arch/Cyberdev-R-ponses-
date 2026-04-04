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
         l'arborescence.

                                                  pwd




        
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
   
_______________________________________________________________________





3.Recherche avancée de fichiers


• trouver tous les fichiers .log 

                                ls *.log 
Permet de lister et de chercher uniquement les fichiers qui ont l' extension <<.log>>




• trouver tous les fichiers de plus de 5 Mo

                               find . -type f -size +5M 
Permet de chercher tous les fichiers mais uniquement ceux qui ont plus de 5M.



• trouver tous les fichiers modifiés il y a moins de 2 jours

                              find . - type f -mtime -2 
cherche tous les fichiers mais seulement ceux qui sont modifiés il y a moins de 2  jours.



• supprimer uniquement les fichiers .tmp

                                         rm *.tmp 
Va supprimer seulement les fichiers qui ont l' extension <<.tmp>>


________________________________________________________________________________________





4.Analyse de contenu


• afficher les 5 premières lignes

                           head -n 5 compte.txt
                           
• afficher les 5 dernières lignes

                           tail -n 5 compte.txt
                           
• compter le nombre total de lignes
                           
                            wc -l compte.txt
                            
• rechercher toutes les lignes contenant le mot ERROR

                            grep "ERROR" compte.txt
                            
• compter combien de fois le mot server apparaît
                                
                            grep -o server compte.txt | wc -l


_______________________________________________________________________







5.Redirection et pipes


• listez les fichiers du répertoire courant et redirigez la sortie vers fichiers.txt

                              ls > fichiers.txt
                           
• ajoutez ensuite la date actuelle dans le même fichier

                              date >> fichiers.txt
                              
• affichez les lignes contenant .sh

                               grep -E .sh$ fichiers.txt
                               
• utilisez un pipe pour compter combien de fichiers .txt existent dans un dossier

                                ls *.txt | wc -l

Expliquez la différence entre > et >>.

La différence entre > et >> : la redirection > redirige la sortie vers un fichier et          écrase ce qui existe déjà. Et la redirection >> ajoute sans écraser le contenu qui existe     ou ajoute à la fin du fichier.


_______________________________________________________________________



6.Processus Linux

• affichez les processus en cour

                    top
• trouvez un processus spécifique par son nom

               ps aux | grep ssh

• expliquez la différence entre PID et PPID

Difference entre PID et PPID : Le PID (Process IDentifier) c'est le numéro unique             attribué à un processus en cours d'exécution sous Linux. Mais le PPID (Parent Process         IDentifier) est le PID du processus « parent », c'est-à-dire celui qui a lancé le             processus actuel. Le PID identifie le processus lui-même, tandis que le PPID identifie        son créateur.



• montrez comment arrêter proprement un processus

                      kill <PID>

• montrez comment forcer l’arrêt d’un processus

                      kill -9 <PID>


_______________________________________________________________________




7.Gestion disque et espaceplei

• afficher l’espace disque total et disponible

           df -h

• afficher la taille d’un dossier précis

          du -sh /home/user/dossier

• identifier les 5 plus gros fichiers d’un répertoire

          du -ah /home | sort -rh | head -n 5

• Expliquer comment détecter rapidement qu’un serveur Linux est presque plein

df -h : en utilisant cette commande, puis on regarde la ligne où est mentionnée <</dev/sda1>> et ensuite on regarde la colonne qui indique le pourcentage d’utilisation du disque mentionné par <<uti%>>. Si le pourcentage est de plus de 90%, cela nous permettra directement de détecter que le serveur linux est presque plein.



_______________________________________________________________________






8.Utilisateurs et groupes

• En utilisant le mode privilégié Via la commande << sudo su >> et ensuite étant dans le        privilégié on utilise la commande <<adduser>>.

                 Exemple : sudo su 
                           adduser jeffuser
                           
• On utilise la commande << sudo groupadd >> . Et dans notre cas pour créer un groupe nommé       devops on procédera de la manière suivante :

                         sudo groupadd devops
                         
• On va utiliser cette commande <<sudo usermod -aG >> afin d'ajouter un
  utilisateur à notre groupe créé. Et on procédera de la manière suivante :

                           sudo usermod -aG devops Paul
                           
• Pour vérifier les groupes d'un utilisateur on va utiliser la commande suivante :

                                   groups Paul
                
• Expliquer pourquoi la bonne gestion des groupes est importante en sécurité
                       
  La bonne gestion des groupes est importante en sécurité parce qu'elle permettra de            renforcer  la sécurité (seuls les utilisateurs autorisés accèdent aux fichiers),une gestion   facile (on   modifie les droits une seule fois pour tout le groupe),moins d’erreurs (évite    de donner trop  de permissions) et une organisation claire (chaque rôle a ses accès)






