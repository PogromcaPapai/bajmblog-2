from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

def atakprzeciwnik():
    return "jeszcze nie zrobiony"

def pominture():
    print('tura')

def lecz():
    print('leczenie')


def walka(eq,hp_gracz,imie,hp_przeciwnik):
    okno = Tk()
    okno.title("Walka")
    okno.geometry("720x600")
    

    # Informacja o HP przeciwnika
    przeciwnik_hp = Label(okno, text=imie+'\nHP: '+str(hp_przeciwnik))
    przeciwnik_hp.place(x=480,y=25)

    # Obraz przeciwnika
    przeciwnik_canvas = Canvas(okno, width = 200, height=200)
    przeciwnik_canvas.place(x=400, y=70)
    przeciwnik_plik=ImageTk.PhotoImage(Image.open('przeciwnik_temp.png'))
    przeciwnik_canvas.create_image(70,70,image=przeciwnik_plik)
    
    #Obraz bohatera
    bohater_canvas = Canvas(okno, width = 200, height=200)
    bohater_canvas.place(x=100, y=200)
    bohater_plik=ImageTk.PhotoImage(Image.open('bohater_temp.png'))
    bohater_canvas.create_image(70,70,image=bohater_plik)

    # Informacja o HP gracza
    bohater_hp = Label(okno, text='\nHP: '+str(hp_gracz))
    bohater_hp.place(x=180,y=405)

    ### Interfejs - defensywa ###
    # Omijanie tury
    przycisk_omin = Button(okno, text="Pomiń turę", command=pominture)
    przycisk_omin.config(height=2,width=13)
    przycisk_omin.place(x= 100, y=450)

    # Poddanie się
    przycisk_poddaj = Button(okno, text="Poddaj się", command=okno.quit)
    przycisk_poddaj.config(height=2,width=13)
    przycisk_poddaj.place(x= 206, y=450)

    # Leczenie
    przycisk_lecz = Button(okno, text="Ulecz się", command=lecz)
    przycisk_lecz.config(height=2, width = 28)
    przycisk_lecz.place(x=100, y=498)

    ### Interfejs - ofensywa ###
    

    okno.mainloop()

walka(['a','b'],1000,'imie',100)