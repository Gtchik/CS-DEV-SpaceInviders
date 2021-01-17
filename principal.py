import tkinter as tk
from Game import Game
from tkinter import  Tk, messagebox

def Start():

    def Restart():
        pnd.destroy()
        PreStart()


    def Apropos():
        messagebox.showinfo("A propos", "Plusieurs cheatcode sont disponible dans ce jeu :\n F1 : Pour se rajouter des vies\n F11: Pour ralentir la vitesse du jeu \n F12 : Pour accélerer la vitesse du jeu")





    pnd=tk.Tk()
    game = Game()

    pnd.title("Space Inviders")

    #Menu Bar
    menubar = tk.Menu(pnd)
    menufichier = tk.Menu(menubar, tearoff=0)
    menufichier.add_command(label= "Redémarrer la partie", command = Restart)
    menufichier.add_command(label= "Quitter", command = pnd.destroy)
    menubar.add_cascade(label="Jeu", menu = menufichier)
    menuaide= tk.Menu(menubar, tearoff=0)
    menuaide.add_command(label = "A propos", command=Apropos)
    menubar.add_cascade(label = "Aide", menu = menuaide)

    pnd.config(menu = menubar)

    #On définit un canvas
    Canvas=tk.Canvas(pnd, height = game.height, width = game.width)
    Canvas.pack(padx=5, pady=5)

    #Démarreur du jeu    
    game.setUp(Canvas).Tick(Canvas, pnd)
  
    pnd.tk.mainloop()

#Fonction qui permet d'affficher la première page
def PreStart():
    def Run():
        pnd.destroy()
        Start()
    pnd=tk.Tk()
    pnd.title("Space Inviders")
    tk.Label(pnd,text='Bienvenue dans notre SpaceInvadeur !').pack()
    tk.Button(pnd,text='Lancer une partie', command=Run).pack()
    tk.Button(pnd,text='Quitter', command=pnd.destroy).pack()
    pnd.mainloop()

PreStart()