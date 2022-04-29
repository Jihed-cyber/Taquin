# Taquin

Auteurs:
Jean Le Mire
Jihed Redjil
Rayan Achibet
Ryan Raad

URL du projet : https://github.com/Jihed-cyber/Taquin

jeu puzzlecomposé de 15 petits carreaux numérotés de 1 à 15 qui glissent dans un cadre prévu pour 16. Il consiste à remettre dans l'ordre les 15 carreaux à partir d'une configuration initiale quelconque. 


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
        
                
