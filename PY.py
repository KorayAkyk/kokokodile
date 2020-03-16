
numerojour=now.strftime("%m%d") 
# lecture fichier fetes
fete=' '
anniv=' '
a=1
f=open('C:/Python25/fetes.txt','r')
while a<366 :
    t=f.readline()
    njour=t.split(',')[0]
if njour == numerojour:
    fete=t.split(',')[1]
    anniv=t.split(',')[2]

    a=a+1
f.close()


txt = "hello, my name is Peter, I am 26 years old"

x = txt.split(", ")

print(x)

txt2 = Label(fen1, bg='yellow',width= 25, text='jour:'+ numerojour, 
anchor='center')
txt3 = Label(fen1, bg='yellow',width0,text='Fêter les ' +fete)
txt4 = Label(fen1, bg='yellow',text=anniv)