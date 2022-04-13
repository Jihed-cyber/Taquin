#######################
# Auteur: Jean Le Mire

########################
# import des librairies

import tkinter as tk
import random as rd


########################
# constantes
HEIGHT = 400
WIDTH = 400

############################
# variables globales
taquin = []
grille= []

####################
# fonctions

def create_taquin():
    """Remplit la liste taquin à deux dimension des entiers de 0 à 15 mélangés"""
    global taquin
    list_entier = list(range(16))
    rd.shuffle(list_entier)
    for i in range(4):
        taquin.append(list_entier[4*i:4*(i+1)])


def display_taquin():
    """Affiche la liste du taquin dans le canevas sous forme de tableau"""


#########################
# partie principale

# création des widgets
root = tk.Tk()
root.title("Taquin")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)

# placement des widgets
canvas.grid(column=1, row=0, rowspan=10)

# boucle principale
root.mainloop()