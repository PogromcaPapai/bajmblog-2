#se robie menu narazie brzydkie i tylko trzy przyciski ale do przodu czy cos 

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

#funkcje przycisków

def autorzy():
    messagebox.showinfo("Twórcy tego cuda","Jakub Dakowski\nNatalia Majda\nWojciech Zięba")
def zacznij_gierke():
    messagebox.showinfo("Rozpocznij gierkę","Za-za-zaczynajmy!")
def baza_bajm():
    print('xD')
def baza_przeciwnik():
    messagebox.showinfo("Zmienić zespół?","Tutaj będzie opcja zmiany przeciwnika but wait")
    print('xD')
def baza_both():
    baza_bajm()
    baza_przeciwnik()


glowneOkno=Tk()

pasekMenu=Menu(glowneOkno)
pierwszeMenu=Menu(pasekMenu,tearoff=0)

pierwszeMenu.add_command(label="Zaktualizuj bazę cytatów",command=baza_both)
pierwszeMenu.add_command(label="Zamknij",command=glowneOkno.quit)
pasekMenu.add_cascade(label="Opcje",menu=pierwszeMenu)

pomocMenu=Menu(pasekMenu,tearoff=0)
pomocMenu.add_command(label="O Autorach",command=autorzy)
pasekMenu.add_cascade(label="Autorzy",menu=pomocMenu)

#daje logo i kocham śledzie

logo_canvas= Canvas(glowneOkno,width=500,height=150)
logo_canvas.pack()
logo_pliczek=ImageTk.PhotoImage(Image.open('logo.gif'))
logo_canvas.create_image(250,60,image=logo_pliczek)

przycisk_rozpoczecie=Button(glowneOkno,text="Rozpocznij grę!",command=zacznij_gierke)
przycisk_rozpoczecie.pack()

zespol = StringVar(glowneOkno, value="https://www.tekstowo.pl/piosenki_artysty,golec_uorkiestra")
zmiana_zespolu_tekst=Label(glowneOkno, text="\nPodaj adres do strony tekstowo.pl wybranego zespołu:")
zmiana_zespolu_tekst.pack()
zmiana_zespolu=Entry(glowneOkno, textvariable=zespol, width=40)
zmiana_zespolu.pack()
zmiana_zespolu_przycisk=Button(glowneOkno, text="Zmień przeciwnika!", command=baza_przeciwnik)
zmiana_zespolu_przycisk.pack()

glowneOkno.config(menu=pasekMenu)
glowneOkno.geometry('960x640')

glowneOkno.mainloop()