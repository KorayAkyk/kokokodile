from tkinter import * 
from tkinter.messagebox import *
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
from datetime import *
import datetime
from datetime import *

def GpExtract():
        
    #
    #  MADE BY KORAY alias KOKO
    #
    #       18/07/2019
    #

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
    cursor1=conn.cursor()
    #ui=tmp.strftime('%Y-%m-%d')
    #uiui=koko.strftime('%Y-%m-%d')
    #
    # string = str.replace(u'\xa0', u'')
    #cursor.execute("select champ1, Ddu from programme where Ddu between ('"+str(tmp)+"') and ('"+str(koko)+"') ORDER BY Ddu DESC")
    #cursor.execute("select champ1, Ddu from programme where Ddu between ('"+str(tmp)+"') and ('"+str(koko)+"') ORDER BY Ddu DESC")
    #cursor.execute("select champ1, Ddu from programme WHERE Ddu Between ('"+str(tmp)+"') and ('"+str(koko)+"')")
    cursor.execute("SELECT LEFT( Ddu, 10 ) , champ1 FROM programme WHERE LEFT(Ddu,10) BETWEEN ('"+str(tmp)+"') and ('"+str(koko)+"') ORDER BY Ddu DESC ")
    # select champ1, Ddu from programme  WHERE Ddu ('2019-07-16') and ('2019-07-25')
    print(koko,tmp)
    #cursor.execute('SELECT champ1 FROM "programme" WHERE "datetime" LIKE \'%' + str(tmp) + '%\'')
    #cursor.execute('select champ1, Ddu from programme where date between to_date(\'%' + str(tmp) + '%''\ ,''YYYY/MM/DD'') and to_date(\'%' + str(koko) + '%\'','YYYY/MM/DD');     
    #cursor.execute('select champ1, Ddu from programme ORDER BY Ddu DESC')

    datetime.datetime.today()
    dateForFile=datetime.datetime.today().strftime('%d-%m-%Y')
    fichier = open(current_dir+"\\data__"+str(dateForFile)+".txt", "a")
    #print(fichier)
    #_____ECRIRE_DANS_LE_FICHIER_TEXTE____________________________________________________________________________________

    for row in cursor.fetchall():
        print(row)
        fichier.write(str(row)+"\n")
    fichier.close()

    #______CORPS_DU_MAIL____________________________________________________________________________________________________

    fromaddr = "koray.akyurek@gardette.com"
    #toaddr=["koray.akyurek@gardette.com","informatique@gardette.com","damien.beauregard@gardette.com"]
    #toaddr1 = "informatique@gardette.com"
    #toaddr2 = "damien.beauregard@gardette.com"
    toaddr3= "koray.akyurek@gardette.com"

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    #msg['To'] = ",".join(toaddr)
    msg['To'] = toaddr3
    msg['Subject'] = "Gp Software Data"
    body = "Python test mail"

    #______PIECE_JOINTE____________________________________________________________________________________________________

    mail_content = """Bonjour c'est Koray, 

    Voici le résultat de l'extraction dans la base de données GP SOFTWARE.

    Cordialement 
    
    AKYUREK Koray """

    #The body and the attachments for the mail
    msg.attach(MIMEText(mail_content, 'plain'))
    # to add an attachment is just add a MIMEBase object
    with open(current_dir+"\\data__"+str(dateForFile)+".txt", 'rb') as f:
        mime = MIMEBase('texte', 'txt', filename="\\data__"+str(dateForFile)+".txt")
        mime.add_header('Content-Disposition', 'attachment', filename="\\data__"+str(dateForFile)+".txt")
        mime.add_header('X-Attachment-Id', '0')
        mime.add_header('Content-ID', '<0>')
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        msg.attach(mime)
    #_______PARAMETRE_MAIL__________________________________________________________________________________________

    server = smtplib.SMTP('smtp.icodia.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("gardette", "t3ygJrc5")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr3, text)
    print('Mail Sent')
    fichier.close()
    os.remove(current_dir+"\\data__"+str(dateForFile)+".txt")

    #____FIN_________________________________________________________________________________________________




"""
fenetre = Tk()
Frame(fenetre, width=600, height=400, borderwidth=1).pack(fill=BOTH)
fenetre.iconbitmap("exe.ico")
fenetre.title('Gp Software Extract')
"""

fen1 = Tk()
Frame(fen1, width=600, height=400, borderwidth=1).pack(fill=BOTH)
fen1.iconbitmap("exe.ico")
fen1.title('Gp Software Extract')


entree = Entry(fen1)#demande la valeur
entree.pack() # integration du widget a la fenetre principale
def saisie():
    print (entree.get()) #recupére la valeur saisie
 
bou1 = Button(fen1, text = 'valider', command = saisie)
bou1.pack()
bou2 = Button(fen1, text = "quitter", command = fen1.destroy)
bou2.pack()
fen1.mainloop()
print (saisie)




fen1.mainloop()