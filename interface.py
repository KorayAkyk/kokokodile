# coding: utf-8
 
from tkinter import * 

fenetre = Tk()

Frame(fenetre, width=600, height=400, borderwidth=1).pack(fill=BOTH)
fenetre.iconbitmap("exe.ico")
fenetre.title('Gp Software Extract')
#fenetre.geometry("800x600")
#fenetre.resizable(width=False, height=False)
#label = Label(fenetre, text="Hello Koko")
#______________________________________________________________________________

from tkinter.messagebox import *


def recupere():
    showinfo("Votre message", entree.get())

value = StringVar() 
value.set("Valeur")
entree = Entry(fenetre, textvariable=str, width=30).place(x=0, y=0)
entree.pack()

bouton = Button(fenetre, text="Valider", command=recupere).place(x=350 ,y=0)
bouton.pack()
# bouton de sortie
bouton=Button(fenetre, text="Fermer", command=fenetre.quit).place(x=400, y=0)
bouton.pack()
def alert():
    showinfo("alerte", "Bravo!")
menubar = Menu(fenetre)
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Créer", command=alert)
menu1.add_command(label="Editer", command=alert)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Couper", command=alert)
menu2.add_command(label="Copier", command=alert)
menu2.add_command(label="Coller", command=alert)
menubar.add_cascade(label="Editer", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar)


#_________________________________________________________________________________
"""
from tkinter.filedialog import *

filepath = askopenfilename(title="Ouvrir une image",filetypes=[('png files','.png'),('all files','.*')])
photo = PhotoImage(file=filepath)
canvas = Canvas(fenetre, width=photo.width(), height=photo.height(), bg="yellow")
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()
"""

#____Fenetre_2____________________________________________________________________________________________

"""
from tkinter import *
fen1 = Tk()
txt1 = Label(fen1, text = 'Nom : ')
txt2 = Label(fen1, text ='Prenom : ')
txt3 = Label(fen1, text ='Age : ')

entr1=Entry(fen1)
entr2=Entry(fen1)
entr3=Entry(fen1)

txt1.grid(row=0)
txt2.grid(row=1)
entr1.grid(row=0,column=1)
entr2.grid(row=1,column=1)
txt3.grid(row=0,column=2)
entr3.grid(row=0,column=3)
"""
#_____________________________________________________________________________________________________

#__________Fenetre_3___________________________________________________________________________
"""
fen2 = Tk()
#
Frame(fen2, width=600, height=400, borderwidth=1).pack(fill=BOTH)
fen2.iconbitmap("exe.ico")
fen2.title('Gp Software Extract')
#fenetre.geometry("800x600")
fen2.resizable(width=False, height=False)
def boutonFourreTout():

    return(0)

bouRouge = Button(fen2, text="FILE", fg="white", bg="red", command = boutonFourreTout)

bouVert = Button(fen2, text="EDIT", fg="white", bg="green", command = boutonFourreTout)

bouBleu = Button(fen2, text="RUN", fg="white", bg="blue", command = boutonFourreTout)

bouNoir = Button(fen2, text="QUIT", fg="white", bg="black", command = boutonFourreTout)


bouRouge.pack(fill=X, ipady=10, padx=10,pady=0)

bouVert.pack(fill=X, ipady=20, padx=10,pady=10)

bouBleu.pack(fill=X, ipady=30, padx=10,pady=10)

bouNoir.pack(fill=X, ipady=60, padx=10,pady=10)
"""
#____________________________________________________________________________________________

fenetre.mainloop()