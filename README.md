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


Tout d'abord, un résumé de ma situation pour vous. Pour la partie de jean de résolution manuel du taquin qui nécessite l'utilisation des fonctions activate et move, il y a un problème car jean bug sur la fonction move et je ne peux pas l'aider car ca nécessite de comprendre la fonction activate qui est la seul fonction que je comprends pas et précisement active_square et number que je comprends absolument pas après des heures car il n'y a pas de texte explicatif. Bonne chance à jean pour finir de coder ceci. Mais ce n'est pas grave car bonne nouvelle au niveau de la résolution automatique qui m'a pris des jours,je suis bien car cela fonctionne avec la fameuse Autoplay(), :) .Le seul problème est qu'il faut que j'installe le module canvas que j'ai pas mais sinon c'est correcte. Donc on a quand meme quelque chose de solide.    Voici l'explication :

Premièrement, la méthode de résolution automatique du taquin que j'ai choisis suit le principe suivant : etape 1 : On passe de l'ordre au désordre, c'est à dire qu'on part de la configuration résolu du taquin donc dans l'ordre naturel. Ensuite,on va provoquer un grand nombre de mouvement aléatoire de la case vide afin d'arriver au désordre,que biensur on enregistre. Au terme de l'étape 1, on a une configuration désordonnée du
taquin, mais en sachant de quels mouvements elle provient. étape 2 : Du désordre à l'ordre : Il suffit de faire les mouvements inverses de la case vide, puisque nous les connaissons et donc obtenir une remise en ordre, on a le taquin résolu. 

Ici, je vous détail le raisonnement. 

Etape 1 :

On part de l’ordre naturel, ce qui revient à mettre dans le tableau a[] (ordre naturel du taquin) les numéros successifs de 0 à l
NP – 1. Pour rappel NP=16 avec N : nombre de ligne, P nombre de colonne à savoir 4*4=16.  

Le tableau inverse pos[]  est un tableau des positions, qui donne la position de chaque numéro. Après répétition de la fonction movcv, on va provoquer un grand nombre de mouvement de la case vide. Par conséquent, la case vide va se déplacé vers ses voisines (haut, gauche, droite, bas) d'ou l'utilité d'une fonction grid() afin de déterminé pour chaque case ses voisines et leur nombre. Pour une  case en position i, les positions de ses voisins sont enregistrées dans le tableau v[i][k] et le nombre de voisins dans nbv[i]. Et pour enregsitrer la direction du voisins on utilise le tableau d[i][k].
Ensuite, on rappele que poscv désigne la position de la case vide à une étape compteur. On choisit au hasard une des nbv[poscv] cases voisines, mais en définissant une variable oldposcv enregistrant l'ancienne position de la case vide pour éviter des aller-retours répétitif. Et selon
la position de la case voisine, que l’on avait enregistrée dans le tableau d[][], on provoque le mouvement correspondant de la case vide. On va mémorisé cette direction dans un tableau b[], ( b[compteur] à l'étape compteur). C'est grace à ce tableau "d'enregistrement" que on enregistre les mouvements pour apres. 
 
 En répétant movcv, on a obtenu le désordre. Il reste plus que répérer la case vide dans le tableau pour la placer en bas à droite ( ordre naturel). On va donc provoquer un déplacement vertical diffvert puis un déplacement horizontal diffhor.
 
 Etape 2 :
 
 Les déplacements de la case vide sont enregistrés dans b[], à l'étape compteur. On a plus qu'a les faires du dernier au premier, et en sens inverse. Exemple, une descente devient une montée etc... définit à l'aide des fonctions monteecv, descentecv, droitecv, gauchecv. Naturelement, on comprend que ces fonctions permettent de monter la case vide, la descendre et ainsi de suite. Les fonctions put_order et disorder permettent de mettre respectivement l'ordre et le désordre. Une petite précision, la nécessité d'écrire une fonction is_tried afin de savoir si le taquin généré est déja trié ou pas, auquel cas pas besoin d'appliquer l'algorithme Solveur pour le résoudre. Ceci est expliquer dans l'algorithme permettant de résoudre le taquin automatiquement: Solveur.  









