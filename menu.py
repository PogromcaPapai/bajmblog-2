#se robie menu narazie brzydkie i tylko trzy przyciski ale do przodu czy cos 

from tkinter import *
from tkinter import messagebox

#funkcje przycisków

def autorzy():
    messagebox.showinfo("Twórcy tego cuda","Jakub Dakowski\nNatalia Majda\nWojciech Zięba")
def zacznij_gierke():
    messagebox.showinfo("Rozpocznij gierkę","Za-za-zaczynajmy!")
def zmien_zespol():
    messagebox.showinfo("Zmienić zespół?","Tutaj będzie opcja zmiany zespołu but wait")


glowne_okno=Tk()
glowne_okno.title("The Bajm Blog RPG")
glowne_okno.geometry("300x250")

przycisk_autorzy=Button(glowne_okno,text="Autorzy",command=autorzy)
przycisk_autorzy.grid()

przycisk_zacznij=Button(glowne_okno,text="Rozpocznij grę",command=zacznij_gierke)
przycisk_zacznij.grid()

przycisk_zespol=Button(glowne_okno,text="Zmień swój zespół",command=zmien_zespol)
przycisk_zespol.grid()

glowne_okno.mainloop()
