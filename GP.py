#
#  MADE BY KORAY alias KOKO
#
#       18/07/2019
#
#______LIBRAIRIES_______________________________________________________________________________________________
import os
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pyodbc
import csv
import datetime
import shutil
import os

current_dir = os.getcwd()
print(current_dir)
src3="G:\Atelier\GP Software Xcap\Data"
src4="D:\\Gardette\\Atelier\\GP Software Xcap\\Data"
src5="\\192.33.50.99\\Gardette\\Atelier\\GP Software Xcap\\Data"
src6="\\192.33.50.99\Gardette\Atelier\GP Software Xcap\Data"
src6=r'\\192.33.50.99\Gardette\Atelier\GP Software Xcap\Data'
shutil.copy(src6+"\\GestProg.mdb" , current_dir )

#___DATE__NOW________________________________________________________________________________________________________

#date1= date.day,date.month,date.year
#print(date1)
#print(datetime)
#date = datetime.datetime.now()
datetime.datetime.today()
koko=datetime.datetime.today().strftime('%Y/%m/%d')
#print(koko) #date aujourd'hui
#print(date)
#print(str(koko)) # date now 


#_____CONNECT_BASE_GP_SOFTWARE____________________________________________________________________________________

#file_dir = os.path.dirname(os.path.abspath(__file__))
from datetime import *
first_date, second_date = date(2018,2,10), date.today()
tmp = first_date
while tmp < second_date:
  #on traite la date comme on veut
  tmp += timedelta(days=1) #on incrémente d'un jour
  #print(tmp)

tmp+=timedelta(days=-7)
tmp=tmp.strftime('%Y/%m/%d')
#print(tmp) #date aujourd'hui -7 jours

current_dir = os.getcwd()
ACCESS_DATABASE_FILE = (current_dir+"\\GestProg.mdb")
#ODBC_CONN_STR= 'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;' % ACCESS_DATABASE_FILE
ODBC_CONN_STR= 'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=%s;' % ACCESS_DATABASE_FILE
conn = pyodbc.connect(ODBC_CONN_STR)
cursor=conn.cursor()
cursor.execute("SELECT LEFT( Ddu, 10 ) , champ1 FROM programme WHERE LEFT(Ddu,10) BETWEEN ('"+str(tmp)+"') and ('"+str(koko)+"') ORDER BY Ddu DESC ")

print(koko,tmp)

from datetime import *
import datetime
datetime.datetime.today()
dateForFile=datetime.datetime.today().strftime('%d-%m-%Y')
fichier = open(current_dir+"\\data__"+str(dateForFile)+".txt", "a")

#_____ECRIRE_DANS_LE_FICHIER_TEXTE____________________________________________________________________________________
data=("Voici l'extraction: "+"\n")
for row in cursor.fetchall():
    print(row)
    fichier.write(str(row)+"\n")
fichier.close()
#os.remove(current_dir+"\\data__"+str(dateForFile)+".txt")




from tkinter import *
from tkinter.messagebox import * # boîte de dialogue

def Verification():
    if Motdepasse.get() == 'gardette':
        # le mot de passe est bon : on affiche une boîte de dialogue puis on ferme la fenêtre
        showinfo('Résultat','Mot de passe correct.\nAu revoir !')
        Mafenetre.destroy()
    else:
        # le mot de passe est incorrect : on affiche une boîte de dialogue
        showwarning('Résultat','Mot de passe incorrect.\nVeuillez recommencer !')
        Motdepasse.set('')

# Création de la fenêtre principale (main window)
Mafenetre = Tk()

Mafenetre.title('Identification requise')
Frame(Mafenetre, width=600, height=400, borderwidth=1).pack(fill=BOTH)
Mafenetre.iconbitmap("exe.ico")
#fenetre.title('Gp Software Extract')

# Création d'un widget Label (texte 'Mot de passe')
Label1 = Label(Mafenetre, text = 'Mot de passe ')
Label1.pack(side = LEFT, padx = 5, pady = 5)

# Création d'un widget Entry (champ de saisie)
Motdepasse= StringVar()
Champ = Entry(Mafenetre, textvariable= Motdepasse, show='*', bg ='bisque', fg='maroon')
Champ.focus_set()
Champ.pack(side = LEFT, padx = 5, pady = 5)

# Création d'un widget Button (bouton Valider)
Bouton = Button(Mafenetre, text ='Valider', command = Verification)
Bouton.pack(side = LEFT, padx = 5, pady = 5)

Label2= Label(Mafenetre, text =(data))
Label2.pack(side = LEFT, padx = 0, pady = 0)
    
    
   
    



Mafenetre.mainloop()
