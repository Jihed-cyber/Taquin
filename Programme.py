#######################
# Auteur: Jean Le Mire

########################
# import des librairies

import tkinter as tk
import random as rd


########################
# constantes

# dimensions du canevas
HEIGHT = 500
WIDTH = 500

# taille du taquin
N = 4

############################
# variables globales
taquin = []
grid_square = []
grid_number = []
taquin_step = []

# position de la case vide dans le taquin
col = 0
lin = 0


####################
# fonctions

def init_taquin():
    """Remplit la liste taquin à deux dimension des entiers de 0 à 15 mélangés."""
    global taquin, taquin_step
    list_entier = list(range(N**2))
    rd.shuffle(list_entier)
    for i in range(N):
        taquin.append(list_entier[N*i:N*(i+1)])
    taquin_step.append(taquin)
    init_grid()


def init_grid():
    """Remplit la liste grid_square avec les identifiant de carrés et la liste grid_number
    affichant le nombre correspondant de la liste taquin
    et affiche les carrés contenant les nombres du taquin dans l'interface graphique"""
    global grid_number, grid_square, taquin
    for i in range(N):
        grid_square.append([0]*N)
        grid_number.append([0]*N)
        for j in range(N):
            largeur = WIDTH // N
            hauteur = HEIGHT // N
            x1 = largeur * i
            y1 = hauteur * j
            x2 = largeur * (i+1)
            y2 = hauteur * (j + 1)
            square = canvas.create_rectangle(x1, y1, x2, y2, fill="grey")
            number = canvas.create_text((x1+x2)//2, (y1+y2)//2, text=taquin[i][j], fill="yellow",
                            font=("Helvetica", 60))
            grid_square[i][j] = square
            grid_number[i][j] = number
    find_index()


def restore_number():
    """Quand le taquin a été modifié, restaure le carré et le nombre à l'emplacement de la case vide"""
    global taquin, lin, col, grid_number, grid_square
    x1 = (WIDTH // N) * col
    y1 = (HEIGHT // N) * lin
    x2 = (WIDTH // N) * (col + 1)
    y2 = (HEIGHT // N) * (lin + 1)
    grid_square[col][lin] = canvas.create_rectangle(x1, y1, x2, y2, fill="grey")
    grid_number[col][lin] = canvas.create_text((x1+x2)//2, (y1+y2)//2, text=taquin[col][lin], fill="yellow",
                                             font=("Helvetica", 60))


def find_index():
    """Trouve l'indice de ligne (lin) et de colonne (col) du 0 dans le taquin
    et supprime le carré et le nombre correspondant à ces indices dans les listes grid_square et grid_number
    pour q'une case vide s'affiche dans l'interface graphique"""
    global taquin, lin, col
    for lists in taquin:
        if 0 in lists:
            lin = lists.index(0)
            col = taquin.index(lists)
    canvas.delete(grid_square[col][lin])
    canvas.delete(grid_number[col][lin])



def refresh_grid():
    """Affiche le taquin de la configuration courante"""
    global grid_number, grid_square, taquin, lin, col
    for i in range(N):
        for j in range(N):
            canvas.itemconfigure(grid_square[i][j], fill="grey")
            canvas.itemconfigure(grid_number[i][j], text=taquin[i][j])
    restore_number()
    find_index()
    


# fonctions de sauvegarde


def save():
    """Ecrit la taille de la grille et les valeurs de la variable
     taquin das le fichier sauvegarde.txt
     """
    global taquin
    fic = open("sauvegarde.txt", "w")
    fic.write(str(N) + "\n")
    for i in range(N):
        for j in range(N):
            fic.write(str(taquin[i][j]) + "\n")
    fic.close()


def load():
    """Lit le fichier sauvegarde.txt et affiche dans l'interface graphique le taquin lu"""
    global N, taquin, taquin_step
    fic = open("sauvegarde.txt", "r")
    taille = fic.readline()
    N = int(taille)
    i = j = 0
    for ligne in fic:
        taquin[i][j] = int(ligne)
        j += 1
        if j == N:
            j = 0
            i += 1
    taquin_step.append(taquin)
    refresh_grid()
    fic.close()


# fonctions evenementielles


def activate(event):
    """Remplit les listes active_square et active_number
    avec les identifiants des objets graphiques que l'utilisateur peut déplacer
    """
    global grid_square, lin, col
    col_mouse = event.x // (WIDTH // N)
    lin_mouse = event.y // (HEIGHT // N)
    refresh_grid()
    active_square = []
    active_number = []
    if col_mouse == col:
        if lin_mouse < lin:
            active_square = grid_square[col][lin_mouse:lin]
            active_number = grid_number[col][lin_mouse:lin]
        if lin_mouse > lin:
            active_square = grid_square[col][lin:lin_mouse+1]
            active_number = grid_number[col][lin:lin_mouse+1]
    if lin_mouse == lin:
        if col_mouse < col:
            for i in range(col_mouse, col):
                active_square.append(grid_square[i][lin])
                active_number.append(grid_number[i][lin])
        if col_mouse > col:
            for i in range(col, col_mouse+1):
                active_square.append(grid_square[i][lin])
                active_number.append(grid_number[i][lin])
    move(active_square, active_number, event.x, event.y)


    

def move(list1, list2, X, Y):
    for i in range(len(list1)):
        canvas.itemconfigure(list1[i], fill="red")
        

# résolution automatique


def resoudre(self):
        "Resoudre le taquin"
        solveur = Solveur(self.taquin)
        res = solveur.resoudre()
        if res == None :
            print ("Pas de solution trouvée")
        else:
            print ("Solution trouvée en ",len(res),"coups")
            self.afficherResult(res)


taquin_2= [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def Numéro_case_vide(self,taquin):
        "Renvoi la position du zero (entier)"
        for i in range(0,len(taquin),1):
            if taquin[i]==0:
                      return i


def testBut(self,taquin):
        "Vérifie si le but est atteint(entier[0,1])"
        if taquin == taquin_2:
            return 1
        else :
            return 0

game=3

def Test(self,taquin):
        "Vérifie si le jeu est déjà en mémoire(entier[0,1])"
        for i in range(0,len(self.open List),1):
            if self.openList[i][game] == taquin :
                return 1



#########################
# partie principale

# création des widgets
root = tk.Tk()
root.title("Taquin")
button_save = tk.Button(root, text="Sauvergarder \n taquin", command=save)
button_load = tk.Button(root, text="Charger taquin", command=load)
button_cancel = tk.Button(root, text="Annuler déplacement")
button_autoplay = tk.Button(root, text="Résoudre  \n automatiquement")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)

# placement des widgets
button_save.grid(row=1, column=0)
button_load.grid(row=1, column=N//4)
button_cancel.grid(row=1, column=2*N//4)
button_autoplay.grid(row=1, column=3*N//4)
canvas.grid(column=0, row=0, columnspan=4)


############################""
# lieu d'essai programme
init_taquin()


# evenementiel
canvas.bind("<Button-1>", activate)

# boucle principale
root.mainloop()