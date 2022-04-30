# Taquin

Auteurs:
Jean Le Mire
Jihed Redjil
Rayan Achibet
Ryan Raad

URL du projet : https://github.com/Jihed-cyber/Taquin

jeu puzzlecomposé de 15 petits carreaux numérotés de 1 à 15 qui glissent dans un cadre prévu pour 16. Il consiste à remettre dans l'ordre les 15 carreaux à partir d'une configuration initiale quelconque. 

Pour ma partie (Jean):

Tout d'abord sont importés les bibliothèques et définis les variables globales et les constantes.

La partie principale du programme est l'endroit où est créé la fenêtre racine, le canvas et les boutons.

Dans cette partie est appelée la fonction init_taquin qui genere un taquin aléatoire, c'est à dire une liste bidimensionnelle contenant les entier de 0 à 15.
La fonction init_taquin appelle la fonction init_grid qui affiche le taquin dans l'interface sous forme de carrés contenant les entiers de la variable taquin (une sous-liste de la variable taquin correspond à une colonne).
La fonction init_grid appelle à son tour la fonction find_index qui attribue aux variables lin et col l'indice de ligne et de colonne du 0 dans le taquin. Cela permet ensuite à  cette fonction de détruire le carré et le nombre 0 correspondant à ces indices pour qu'une case vide s'affiche à la place.

Le bouton sauvegarde appelle la fonction save qui écrit le taquin courant dans un fichier texte afin qu'on puisse ensuite le recharger via le bouton charger qui appelle la fonction load.
La fonction load lit le fichier sauvegarde.txt et modifie la variable globale taquin en conséquence. Elle appelle ensuite la fonction refresh_grid pour que l'interface affiche le taquin chargé. La fonction refresh_grid crée un nouveau carré et nombre à la place de la case vide puis appelle elle aussi la fonction find_index (on évite la duplication du code)

Quand on clique à un endroit du taquin les cases déplaçables s'affiche en rouge le cas échéant. Ceci est réalisé par la fonction activate appelé dans la méthode bind de la partie principale. La fonction activate appelle la fonction move qui doit permettre le déplacement de la/les cases sélectionnés avec la souris (ce sur quoi je galère).

Voici ce que j'ai fait ( Jihed) :

Déja le code pour le jeu taquin mais manuellement (je sais pas si jean a fait).

Voici une proposition pour la résolution du taquin :

Déja on utilise self : c'est une variable qui référence l'ojbjet choisit, pour pouvoir accéder aux classes. ET Une classe définit des attributs et des méthodes. Genre par ex, class de résolution à l'intérieur on met tout les fonctions pour résoudre le taquin. Voici les fonctions que j'ai déja. Il y a 2-3 erreur de syntaxe mais c'est mon ordianteur qui bug. Les voici: 



def resoudre(self):
        "Resoudre le taquin"
        solveur = Solveur(self.taquin)
        res = solveur.resoudre()
        if res == None :
            print ("Pas de solution trouvee")
        else:
            print ("Solution trouvee en ",len(res),"coups")
            self.afficherResult(res)


taquin_2= [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def Numéro_case_vide(self,taquin):
        "Renvoi la position du zero (entier)"
        for i in range(0,len(taquin),1):
            if taquin[i]==0:
              return i





def testBut(self,taquin):
        "Verifie si le but est atteint(entier[0,1])"
        if taquin == taquin_2:
            return 1
        else :
            return 0

game=3

def Test(self,taquin):
        "Verifie si le jeu est deja en memoire(entier[0,1])"
        for i in range (0,len(self.openList),1):
            if self.openList[i][game] == taquin :
                return 1
        
                
