#######################
# Auteur: Jean Le Mire

########################
# import des librairies

import tkinter as tk
import random as rd


########################
# constantes

# dimensions du canevas
#HEIGHT = 400
#WIDTH = 400

# taille du taquin
N = 4

############################
# variables globales
taquin = []
grille= []

# indices de la case vide
# ligne
a = N
# colonne
b = N

####################
# fonctions

def init_taquin():
    """Remplit la liste taquin à deux dimension des entiers de 0 à 15 mélangés."""
    global taquin
    list_entier = list(range(N**2))
    rd.shuffle(list_entier)
    for i in range(N):
        taquin.append(list_entier[N*i:N*(i+1)])


def init_grille():
    """Remplit la liste grille avec les identifiant de labels
    affichant le nombre correspondant de la liste taquin."""
    global grille, taquin
    for i in range(N):
        grille.append([0]*N)
        for j in range(N):
            number = tk.Label(root, text=taquin[i][j], font=("helvetica", "80"), width=2,
            relief="groove", activebackground="red")
            grille[i][j] = number


def display_taquin():
    """Place les label de la liste grille pour que le taquin s'affiche dans l'interface graphique."""
    global grille, taquin
    for i in range(N):
        for j in range(N):
            grille[i][j].grid(column=10*i, row=10*j, columnspan=10, rowspan=10)
    for list in taquin:
        if 0 in list:
            b = list.index(0)
            a = taquin.index(list)
    grille[a][b].grid_forget()


def save():
    """Ecrit la taille de la grille et les valeurs de la variable
     taquin das le fichier sauvegarde.txt
     """
    fic = open("sauvegarde.txt", "w")
    fic.write(str(N) + "\n")
    for i in range(N):
        for j in range(N):
            fic.write(str(taquin[i][j]) + "\n")
    fic.close()


def load():
    """Lit le fichier sauvegarde.txt et affiche dans l'interface graphique le taquin lu"""
    global N
    fic = open("sauvegarde.txt", "r")
    taille = fic.readline()
    N = int(taille)
    init_taquin()
    i = j = 0
    for ligne in fic:
        taquin[i][j] = int(ligne)
        j += 1
        if j == N:
            j = 0
            i += 1
    init_grille()
    display_taquin()
    fic.close()


def activate(event):
    global grille, a, b
    b_souris = event.x // 120
    a_souris = event.y // 120
    if b_souris == b:
        if a_souris < a:
            for i in range(a_souris, a):
                grille[i][b].configure(state="active")
        if a_souris > a:
            for i in range(a, a_souris+1):
                grille[i][b].configure(state="active")
    if a_souris == a:
        if b_souris < b:
            for i in range(b_souris, b):
                grille[a][i].configure(state="active")
        if b_souris > b:
            for i in range(b, b_souris+1):
                grille[a][i].configure(state="active")
    init_grille()
    display_taquin()




#########################
# partie principale

# création des widgets
root = tk.Tk()
root.title("Taquin")
button_save = tk.Button(root, text="Sauvergarder \n taquin", command=save)
button_load = tk.Button(root, text="Charger taquin", command=load)
button_cancel = tk.Button(root, text="Annuler déplacement")
button_autoplay = tk.Button(root, text="Résoudre  \n automatiquement")
#canvas = tk.Canvas(root, height=400, width=400)

# placement des widgets
button_save.grid(row=10*N+1, column=0, columnspan=10)
button_load.grid(row=10*N+1, column=10*N//4, columnspan=10)
button_cancel.grid(row=10*N+1, column=20*N//4, columnspan=10)
button_autoplay.grid(row=10*N+1, column=30*N//4, columnspan=10)
#canvas.grid(column=0, row=41, rowspan=40)


############################""
# lieu d'essai programme
init_taquin()
init_grille()
display_taquin()

# evenementiel
root.bind("<Button-1>", activate)

# boucle principale
root.mainloop()