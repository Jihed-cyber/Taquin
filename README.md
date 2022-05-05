# Taquin

Auteurs:
Jean Le Mire
Jihed Redjil
Rayan Achibet
Ryan Raad

URL du projet : https://github.com/Jihed-cyber/Taquin

jeu puzzle composé de 15 petits carreaux numérotés de 1 à 15 qui glissent dans un cadre prévu pour 16. Il consiste à remettre dans l'ordre les 15 carreaux à partir d'une configuration initiale quelconque. 

Pour ma partie (Jean):

Tout d'abord sont importés les bibliothèques et définis les variables globales et les constantes.

La partie principale du programme est l'endroit où est créé la fenêtre racine, le canvas et les boutons.

Dans cette partie est appelée la fonction init_taquin qui genere un taquin aléatoire, c'est à dire une liste bidimensionnelle contenant les entier de 0 à 15.
La fonction init_taquin appelle la fonction init_grid qui affiche le taquin dans l'interface sous forme de carrés contenant les entiers de la variable taquin (une sous-liste de la variable taquin correspond à une colonne).
La fonction init_grid appelle à son tour la fonction find_index qui attribue aux variables lin et col l'indice de ligne et de colonne du 0 dans le taquin. Cela permet ensuite à  cette fonction de détruire le carré et le nombre 0 correspondant à ces indices pour qu'une case vide s'affiche à la place.

Le bouton sauvegarde appelle la fonction save qui écrit le taquin courant dans un fichier texte afin qu'on puisse ensuite le recharger via le bouton charger qui appelle la fonction load.
La fonction load lit le fichier sauvegarde.txt et modifie la variable globale taquin en conséquence. Elle appelle ensuite la fonction refresh_grid pour que l'interface affiche le taquin chargé. La fonction refresh_grid crée un nouveau carré et nombre à la place de la case vide puis appelle elle aussi la fonction find_index (on évite la duplication du code)

Quand on clique à un endroit du taquin les cases déplaçables s'affiche en rouge le cas échéant. Ceci est réalisé par la fonction activate appelé dans la méthode bind de la partie principale. La fonction activate appelle la fonction move qui doit permettre le déplacement de la/les cases sélectionnés avec la souris (ce sur quoi je galère).



Pour ma partie (Jihed):

# résolution automatique du taquin.


Tout d'abord, un résumé de ma situation pour vous. Pour la partie de jean de résolution manuel du taquin qui nécessite l'utilisation des fonctions activate et move, il y a un problème car jean bug sur la fonction move et je ne peux pas l'aider car ca nécessite de comprendre la fonction activate qui est la seul fonction que je comprends pas et précisement active_square et number que je comprends absolument pas après des heures car il n'y a pas de texte explicatif. Bonne chance à jean pour finir de coder ceci. Mais ce n'est pas grave car bonne nouvelle au niveau de la résolution automatique qui m'a pris des jours,je suis bien car cela fonctionne. Le seul problème est qu'il faut que j'installe le module canvas que j'ai pas mais sinon c'est correcte. Donc on a quand meme quelque chose de solide. Voici l'explication :


                
