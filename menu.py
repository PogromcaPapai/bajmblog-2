#se robie menu narazie brzydkie i tylko trzy przyciski ale do przodu czy cos 

from tkinter import *
from tkinter import messagebox

#funkcje przycisków

def autorzy():
    messagebox.showinfo("Twórcy tego cuda","Jakub Dakowski\nNatalia Majda\nWojciech Zięba")
def zacznij_gierke():
    messagebox.showinfo("Rozpocznij gierkę","Za-za-zaczynajmy!")
def zmien_zespol():
    messagebox.showinfo("Zmienić zespół?","Tutaj będzie opcja zmiany przeciwnika but wait")


glowneOkno=Tk()

pasekMenu=Menu(glowneOkno)
pierwszeMenu=Menu(pasekMenu,tearoff=0)


pierwszeMenu.add_command(label="Zmień przeciwnika",command=zmien_zespol)
pierwszeMenu.add_command(label="Zamknij",command=glowneOkno.quit)
pasekMenu.add_cascade(label="Opcje",menu=pierwszeMenu)

pomocMenu=Menu(pasekMenu,tearoff=0)
pomocMenu.add_command(label="O Autorach",command=autorzy)
pasekMenu.add_cascade(label="Autorzy",menu=pomocMenu)

przycisk_rozpoczecie=Button(glowneOkno,text="Rozpocznij grę!",command=zacznij_gierke)
przycisk_rozpoczecie.place(x=60,y=70)

glowneOkno.config(menu=pasekMenu)
glowneOkno.mainloop()
