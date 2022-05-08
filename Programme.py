#######################
# Auteur: Jean Le Mire, Jihed Redjil

########################
# import des librairies

import tkinter as tk
from random import randint, shuffle
from copy import deepcopy
from functools import partial


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
    shuffle(list_entier)
    list_test = list_entier[:]
    while resolvable(list_test) == False:
        shuffle(list_test)
    for i in range(N):
        taquin.append(list_entier[N*i:N*(i+1)])
    init_grid()


def resolvable(list_mixed):
    """Compte le nombre de permutations nécessaires entre les entiers de la liste des entiers mélangés
    (liste qui servirait à construire la list bidimensonnelle taquin)
    pour obtenir la liste des entiers correspondant au taquin résolu,
    et renvoie True si la configuration serait résolvable et False sinon
    """
    taquin_solved = []
    taquin_solved = list(range(1,N**2))
    taquin_solved.append(0)
    permutation = 0
    while list_mixed != taquin_solved:
        for i in range(N**2):
            if list_mixed[i] != taquin_solved[i]:
                wrong_index = list_mixed.index(taquin_solved[i])
                list_mixed[i], list_mixed[wrong_index] = list_mixed[wrong_index], list_mixed[i]
                permutation += 1
    if permutation % 2 == 0:
        return True
    else:
        return False


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
    new_step()
    print(taquin_step)


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
    refresh_grid()
    fic.close()



# commande du bouton annuler déplacement


def new_step():
    """Chaque fois que le taquin est modifié, ajoute le taquin courant dans la liste taquin_step"""
    global taquin_step, taquin
    current_taquin = deepcopy(taquin)
    if taquin_step == []:
        taquin_step.append(current_taquin)
    else:
        if current_taquin != taquin_step[-1]:
            taquin_step.append(current_taquin)
    

def cancel_move():
    """Permet d'annuler le cas échéant un déplacement
    en revenant à la configuration du taquin antérieure
    """
    global taquin_step, taquin
    if len(taquin_step) >= 2:
        taquin = taquin_step[-2]
        del taquin_step[-1]
        refresh_grid()



# fonctions evenementielles


def activate(event):
    """Remplit les listes active_square et active_number
    avec les identifiants des objets graphiques que l'utilisateur peut déplacer
    """
    global taquin, grid_square, grid_square, lin, col
    col_mouse = event.x // (WIDTH // N)
    lin_mouse = event.y // (HEIGHT // N)
    refresh_grid()
    active_square = []
    active_number = []
    active_taquin = []
    if col_mouse == col:
        if lin_mouse < lin:
            active_square = grid_square[col][lin_mouse:lin]
            active_number = grid_number[col][lin_mouse:lin]
            active_taquin = taquin[col][lin_mouse:lin]
            direction = "bas"
        if lin_mouse > lin:
            active_square = grid_square[col][lin:lin_mouse+1]
            active_number = grid_number[col][lin:lin_mouse+1]
            active_taquin = taquin[col][lin+1:lin_mouse+1]
            direction = "haut"
    if lin_mouse == lin:
        if col_mouse < col:
            for i in range(col_mouse, col):
                active_square.append(grid_square[i][lin])
                active_number.append(grid_number[i][lin])
                active_taquin.append(taquin[i][lin])
            direction = "droite"
        if col_mouse > col:
            for i in range(col+1, col_mouse+1):
                active_square.append(grid_square[i][lin])
                active_number.append(grid_number[i][lin])
                active_taquin.append(taquin[i][lin])
            direction = "gauche"
    movable(active_square, active_number, active_taquin, direction)


def movable(list_square, list_number, list_taquin, direction):
    """Colorie les cases que le joueur va déplacer en rouge,
    initialise les listes qui contiendront les coordonnées successives de la souris pendant le déplacement
    et lie l'évènement relâchage du bouton de la souris à want_move
    et l'évènement déplacement de la souris à get_move
    """
    for i in range(len(list_square)):
        canvas.itemconfigure(list_square[i], fill="red")
    list_abscissa = []
    list_ordonate = []
    canvas.bind("<ButtonRelease-1>", want_mvt)
    canvas.bind("<Motion>", partial(get_move, list_x=list_ordonate, list_y=list_abscissa, dir=direction,
    squares = list_square, numbers=list_number, taquin_select=list_taquin))


def want_mvt(event):
    """Détecte si la souris a été relâché
    ce qui signifie le cas échéant que l'utilisateur ne souhaite pas déplacer les cases présélectionnées,
    donc annule le déplacement en cours
    """
    global grid_number, grid_square
    canvas.unbind("<Motion>")
    for i in range(N):
        for j in range(N):
            canvas.delete(grid_square[i][j])
            canvas.delete(grid_number[i][j])        
    init_grid()


def get_move(event, list_x, list_y, dir, squares, numbers, taquin_select):
    """Récupère les coordonnées de la souris lorsqu'on la bouge
    et déplace les cases suivant le mouvment de la souris,
    puis actualise le taquin et les grilles en fonction du déplacement
    """
    global taquin
    list_x.append(event.x)
    list_y.append(event.y)
    col_mouse = list_x[0] // (WIDTH // N)
    lin_mouse = list_y[0] // (HEIGHT // N)
    dx, dy = 0, 0
    if len(list_x) >= 2:
        dx = list_x[-1] - list_x[-2]
    if len(list_y) >= 2:
        dy = list_y[-1] - list_y[-2]
    if dir == "haut" and dy <= 0: # or dir == "bas" and dy>= 0
        if dy <= 0:
            move_vertical(move_square=squares, move_number=numbers, lin_clic=lin_mouse, move_y=list_y, dy=dy)
    if dir == "bas":
        if dy >= 0:
            move_vertical(move_square=squares, move_number=numbers, lin_clic=lin_mouse, move_y=list_y, dy=dy)
    if dir == "gauche":
        if dx <= 0:
            move_horizontal(move_square=squares, move_number=numbers, move_taquin=taquin_select,
            col_clic=col_mouse, lin_clic=lin_mouse, move_x=list_x, dx=dx, direction="gauche")
    if dir == "droite":
        if dx >= 0:
             move_horizontal(move_square=squares, move_number=numbers, move_taquin=taquin_select,
            col_clic=col_mouse, lin_clic=lin_mouse, move_x=list_x, dx=dx, direction="droite")          
    

def move_vertical(move_square, move_number, lin_clic, move_y, dy):
    """Déplace les cases suivant le mouvment de la souris dans le cas d'un mouvement vertical
    puis actualise le taquin et les grilles en fonction du déplacement
    """
    global taquin
    for i in range(len(move_square)):
        canvas.move(move_square[i], 0, dy)
        canvas.move(move_number[i], 0, dy)
        if (move_y[-1] - move_y[0]) ** 2 >= ((HEIGHT // N) // 1.2) ** 2:
            taquin[col].remove(0)
            taquin[col].insert(lin_clic, 0)
            refresh_grid()
            canvas.unbind("<Motion>")


def move_horizontal(move_square, move_number, move_taquin, col_clic, lin_clic, move_x, dx, direction):
    """Déplace les cases suivant le mouvment de la souris dans le cas d'un mouvement vertical
    puis actualise le taquin et les grilles en fonction du déplacement
    """
    global taquin
    for i in range(len(move_square)):
        canvas.move(move_square[i], dx, 0)
        canvas.move(move_number[i], dx, 0)
        if (move_x[-1] - move_x[0]) ** 2 >= ((HEIGHT // N) // 1.2) ** 2:
            taquin[col_clic][lin_clic] = 0
            for i in range(len(move_taquin)):
                if direction == "droite":
                    taquin[col-i][lin] = move_taquin[-1-i]
                if direction == "gauche":
                    taquin[col+i][lin] = move_taquin[i]
            refresh_grid()
            canvas.unbind("<Motion>")




# résolution automatique


<<<<<<< HEAD
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
pos = [15, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
=======
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
pos=[15,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
>>>>>>> 8d102860e82216b4ddfda133dcabf3ff65f17c57

nbv = [0 for i in range (0,16)]
v = [[0 for i in range (0,4)] for j in range (0,16)]
d = v


def grid():
    """détermine pour chaque case quelles sont ses voisines ainsi que leur nombre."""
    for i in range (0,16):
        k = 0
        if (i+1)%4 != 0:
            v[i][k] = i + 1
            d[i][k] = 0
            k = k+1
        if i%N != 0:
            v[i][k] = i - 4
            d[i][k] = 1
            k =  k + 1
        if i < 12:
            v[i][k] = i + N
            d[i][k] = 3
            k = k + 1
            nbv[i] = k


def find_case_vide(taquin):
    """Trouver la position de la case vide d'indice 0"""
    for i in range(0,16):
        if taquin[i] == 0:
            return i

<<<<<<< HEAD

#poscv =  find_case_vide(taquin)
#oldposcv= poscv
b = []
=======
poscv =  find_case_vide(taquin)
oldposcv= poscv
b=[]
>>>>>>> 8d102860e82216b4ddfda133dcabf3ff65f17c57
compteur = 0


#v: liste qui contient les voisins des indices de chaque chiffre


def movcv():
<<<<<<< HEAD
    """faire bouger la case vide par mouvement aléatoire afin de créer le désordre"""
    h = 0
    compteur = 0
    while v[poscv][h] == oldposcv:
        h = randint(0,nbv[poscv])
    b[compteur] = d[poscv][h]
    if d[poscv][h] == 0:
        droitecvl()
    elif d[poscv][h] == 1:
        monteecv()
    elif d[poscv][h] == 2:
        gauchecv()
    elif d[poscv][h] == 3:
=======
    h=0
    compteur=0
    while(v[poscv][h]==oldposcv):
        h=random.randint(0,nbv[poscv])
    b[compteur]= d[poscv][h]
    if (d[poscv][h]==0):
        droitecvl()
    elif (d[poscv][h]==1):
        monteecv()
    elif (d[poscv][h]==2):
        gauchecv()
    elif (d[poscv][h]==3):
>>>>>>> 8d102860e82216b4ddfda133dcabf3ff65f17c57
        descentecv()


<<<<<<< HEAD
NP = 16


def droitecvl():
    """Faire bouger la case vide vers la droite"""
    a[poscv] = a[poscv+1]
    pos[a[poscv]] = poscv
    poscv = poscv + 1
    a[poscv] = 15
    pos[15] = poscv

=======
def droitecvl():
    a[poscv]=a[poscv+1]
    pos[a[poscv]]=poscv
    poscv=poscv+1
    a[poscv]=15
    pos[15]=poscv
>>>>>>> 8d102860e82216b4ddfda133dcabf3ff65f17c57

def gauchecv():
    """faire bouger la case vide vers la gauche"""
    a[poscv] = a[poscv-1]
    pos[a[poscv]] = poscv
    poscv = poscv - 1
    a[poscv] = NP - 1
    pos[NP-1]= poscv


def descentecv():
    """Faire bouger la case vide vers le bas"""
    a[poscv] = a[poscv+N]
    pos[a[poscv]] = poscv
    poscv = poscv + N
    a[poscv] = NP - 1
    pos[NP-1] = poscv


def monteecv():
    """Faire bouger la case vide vers le haut"""
    a[poscv] = a[poscv-N]
    pos[a[poscv]] = poscv
    poscv = poscv - N
    a[poscv] = NP - 1
    pos[NP-1] = poscv


def put_disorder():
    """mettre le désordre (voir détail de chaque étape de la fonction à chaque ligne)"""
    for i in range (0,16):
        a[i] = i # rectangle avec l’ordre naturel pour les blocs carrés
    grid()
<<<<<<< HEAD
    oldposcv = -1
    poscv = NP - 1 #conditions initiales pour la case vide, qui a deux possibilités de mouvements,
=======
    oldposcv= -1
    poscv=NP-1 #conditions initiales pour la case vide, qui a deux possibilités de mouvements,
>>>>>>> 8d102860e82216b4ddfda133dcabf3ff65f17c57
        # la valeur initiale de oldpcv ne provoquant aucun empêchement
    for i in range (0,30000):
        movcv()      # déplacements répétés de la case vide */
        diffvert = P - 1 - poscv / N #différence verticale entre la position actuelle et la position finale de la case vide */
        if taquin == a:
            break
    for i in range (0, diffvert):
        descentecv()  
        compteur += 1
        b[compteur] = 3 #mémorisation des mouvememts dans b[] */
        diffort = N - 1 - poscv % N  #de même horizontalement */
    for i in range (0, diffort):
        droitecv()
        compteur += 1
        b[compteur] = 0


def put_order():
    """remettre l'ordre en appelant les fonctions droitecv, descentecv, monteecv, gauchecv"""
    for i in range(0,compteur,-1):
        if b[i] == 0:
            gauchecv()
        elif b[i] == 1:
            descentecv()
        elif b[i] == 2:
            droitecv()
        elif b[i] == 3:
            monteecv()


def is_tried():
    """Savoir si la liste bidimensionel donc le taquin est trié ou non"""
    for i in range(0,15):
        if taquin[i] > taquin[i+1]:
            return False
    return True

<<<<<<< HEAD

def Solveur():
    """ Dans l'hypothèse où le taquin a été créé
    algorithme principal utilisant put_order et disorder afin de résoudre le taquin
    """
=======
def Solveur():
    """ Dans l'hypothèse où le taquin a été créé """
>>>>>>> 8d102860e82216b4ddfda133dcabf3ff65f17c57
    if is_tried() is True:
        print("La liste est déjà trié :)")
        return None
    else:
        grid()
        poscv = find_case_vide(taquin)
        oldposcv = poscv
        put_disorder()
        put_order()
        print("a = ",a)
        print("taquin = ",taquin)


 # grid :détermine pour chaque case quelles sont ses voisines ainsi que leur nombre.
# find_case_vide : Trouver la position de la case vide d'indice 0
# is_tried : Savoir si la liste bidimensionel donc le taquin est trié ou non
# movcv : faire bouger la case vide par mouvement aléatoire afin de créer le désordre
# droitecv : Faire bouger la case vide vers la droite
# gauchecv : faire bouger la case vide vers la gauche
# monteecv : la faire bouger vers le haut
# descentecv : la faire bouger vers le bas
# put_disorder: mettre le désordre ( voir détail de chaque étape de la fonction à chaque ligne)
# put_order : remettre l'ordre en appelant les fonctions droitecv, descentecv, monteecv, gauchecv
# Solveur : Algorithme principal utilisant put_order et disorder afin de résoudre le taquin 


#########################
# partie principale

# création des widgets
root = tk.Tk()
root.title("Taquin")
button_save = tk.Button(root, text="Sauvergarder \n taquin", command=save)
button_load = tk.Button(root, text="Charger taquin", command=load)
button_cancel = tk.Button(root, text="Annuler déplacement", command=cancel_move)
button_autoplay = tk.Button(root, text="Résoudre  \n automatiquement")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)

# placement des widgets
button_save.grid(row=1, column=0)
button_load.grid(row=1, column=N//4)
button_cancel.grid(row=1, column=2*N//4)
button_autoplay.grid(row=1, column=3*N//4)
canvas.grid(column=0, row=0, columnspan=4)

# initialisation du taquin
init_taquin()

# evenementiel
canvas.bind("<Button-1>", activate)

# boucle principale
root.mainloop()
