from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

class jednostka():
    ####
    # Zadaniem klasy jest tworzenie jednostek do walki
    ####
    def __init__(self, imie, gracz=False):
        self.imie=imie
        if gracz==True:
            self.hp='1000'
            fota=Image.open('test.jpg')
        else:
            self.hp='100'
            fota=Image.open('przeciwnik_temp.png')
        fota=fota.resize((250,250),Image.ANTIALIAS)
        self.obraz=ImageTk.PhotoImage(image=fota)

    def zwrochp(self):
        return self.hp
    
    def zwrocobraz(self):
        return self.obraz
    
    def zwrocimie(self):
        return self.imie

class Walka(Frame):
    def atakprzeciwnik(self):
        print('atak')

    def pominture(self):
        print('tura')

    def lecz(self):
        print('leczenie')

    def __init__(self,master,imie_boh,imie_przec):
        ####
        # Kod rozpoczynający walkę
        ####
        Frame.__init__(self, master)
        self.master = master
        self.gracz = jednostka(imie_boh,gracz=True)
        self.przeciwnik = jednostka(imie_przec)
        self.zbudujprzeciwnika()
        self.zbudujbohatera()

    def zbudujprzeciwnika(self):
        ####
        # Tworzy obszar wyświetlający przeciwnika
        ####
        rama = Frame(self)

        # Informacje
        hp = Label(rama, text=self.przeciwnik.zwrocimie()+'\nHP: '+self.przeciwnik.zwrochp())
        hp.pack()
        
        # Obraz
        plotno = Label(rama, image=self.przeciwnik.zwrocobraz())
        plotno.pack()
        rama.place(relx=0.65,rely=0.01)

    def zbudujbohatera(self):
        ####
        # Tworzy obszar wyświetlający gracza
        ####
        rama = Frame(self)
        
        # Obraz
        plotno = Label(rama, image=self.gracz.zwrocobraz())
        plotno.pack()

        # Informacje
        hp = Label(rama, text=self.gracz.zwrocimie()+'\nHP: '+self.gracz.zwrochp())
        hp.pack()
        
        rama.place(relx=0.1,rely=0.3)



okno = Tk()
okno.geometry('960x640')
Walka(okno,'gracz','kot').place(relwidth=1,relheight=1)
okno.mainloop()