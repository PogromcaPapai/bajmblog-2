from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

class Walka(Frame):
    def atakprzeciwnik(self):
        return "jeszcze nie zrobiony"

    def pominture(self):
        print('tura')

    def lecz(self):
        print('leczenie')

    def __init__(self,master,eq,lvl,imie_boh,imie_przec):
        Frame.__init__(self, master)
        self.master = master
        self.hp_gracz = 1000
        self.imie_gracz = imie_boh
        self.imie_przec = imie_przec
        self.hp_przec=100

        przeciwnik = Frame(self)
        przeciwnik_hp = Label(przeciwnik, text=self.imie_przec+'\nHP: '+str(self.hp_przec))
        przeciwnik_hp.pack()

        # Obraz przeciwnika
        przeciwnik_canvas = Canvas(przeciwnik, width = 200, height=200)
        przeciwnik_canvas.pack()
        przeciwnik_plik=ImageTk.PhotoImage(Image.open('przeciwnik_temp.png'))
        przeciwnik_canvas.create_image(70,70,image=przeciwnik_plik)

        przeciwnik.pack(side=LEFT)
        #Obraz bohatera
        bohater_canvas = Canvas(self, width = 200, height=200)
        bohater_canvas.place(x=100, y=200)
        bohater_plik=ImageTk.PhotoImage(Image.open('bohater_temp.png'))
        bohater_canvas.create_image(70,70,image=bohater_plik)

        # Informacja o HP gracza
        bohater_hp = Label(self, text='\nHP: '+str(self.hp_gracz))
        bohater_hp.place(x=180,y=405)

        ### Interfejs - defensywa ###
        # Omijanie tury
        przycisk_omin = Button(self, text="Pomiń turę")
        przycisk_omin.config(height=2,width=13)
        przycisk_omin.place(x= 100, y=450)

        # Poddanie się
        przycisk_poddaj = Button(self, text="Poddaj się", command=self.quit)
        przycisk_poddaj.config(height=2,width=13)
        przycisk_poddaj.place(x= 206, y=450)

        # Leczenie
        przycisk_lecz = Button(self, text="Ulecz się")
        przycisk_lecz.config(height=2, width = 28)
        przycisk_lecz.place(x=100, y=498)

        ### Interfejs - ofensywa ###


okno = Tk()
okno.geometry('960x720')
Walka(okno,[1,2],1,'pies','kot').pack()
okno.mainloop()