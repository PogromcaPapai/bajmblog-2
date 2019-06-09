#Import - UI
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
#Import - cytaty
import sqlite3
#Import - reszta
import random

'''
Konstrukcja interfejsu walki
'''

class jednostka():
    ####
    # Zadaniem klasy jest tworzenie jednostek do walki
    ####
    def __init__(self, imie, gracz=False):
        self.imie=imie
        self.hp=IntVar()
        if gracz==True:
            self.hp.set(1000)
            fota=Image.open('test.jpg')
        else:
            self.hp.set(100)
            fota=Image.open('przeciwnik_temp.png')
        fota=fota.resize((250,250),Image.ANTIALIAS)
        self.obraz=ImageTk.PhotoImage(image=fota)

    def zwrochp(self):
        return str(self.hp.get())
    
    def zwrocobraz(self):
        return self.obraz
    
    def zwrocimie(self):
        return self.imie

class Walka(Frame):
    def atakuj(self):
        czym = self.wybrana.get()
        print('atak',czym)
        self.event_generate('<BackSpace>')

    def pominture(self):
        print('tura')
        self.event_generate('<BackSpace>')

    def lecz(self):
        self.gracz.hp.set(self.gracz.hp.get()+10)
        messagebox.showinfo("Leczenie", self.gracz.zwrochp())
        self.event_generate('<BackSpace>')

    def __init__(self,master,gracz,przeciwnik):
        ####
        # Kod rozpoczynający walkę
        ####
        Frame.__init__(self, master)
        self.master = master
        self.gracz = gracz
        self.przeciwnik = przeciwnik
        self.zbudujprzeciwnika()
        self.zbudujgracza()
        self.zbudujdefensywa()
        self.zbudujofensywa()

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

    def zbudujgracza(self):
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
        
        rama.place(relx=0.1, rely=0.3)

    def zbudujdefensywa(self):
        ####
        # Tworzy przyciski z opcjami defensywnymi
        ####
        rama = Frame(self)

        # Omijanie tury
        przycisk_omin = Button(rama, text="Pomiń turę", command=self.pominture)
        przycisk_omin.config(height=2,width=16)
        przycisk_omin.grid(row=0,column=0)

        # Poddanie się
        przycisk_poddaj = Button(rama, text="Poddaj się", command=self.quit)
        przycisk_poddaj.config(height=2,width=16)
        przycisk_poddaj.grid(row=0,column=1)

        # Leczenie
        przycisk_lecz = Button(rama, text="Ulecz się", command=self.lecz)
        przycisk_lecz.config(height=2, width = 34)
        przycisk_lecz.grid(row=1,column=0,columnspan=2)

        rama.place(relx=0.1, rely=0.8)
    
    def zbudujofensywa(self):
        ####
        # Tworzy przycisk ataku i menu wyboru utworów
        ####
        rama = Frame(self)
        
        # Dropdown menu
        opcje = {'pies','kot','arka'}
        self.wybrana = StringVar(self, 'Wybierz broń')
        polewyboru = OptionMenu(rama, self.wybrana, *opcje)
        polewyboru.config(height=2, width = 34)
        polewyboru.grid(column=0,row=0)

        # Przycisk ataku
        przycisk_atak = Button(rama, text="Atakuj", command=self.atakuj)
        przycisk_atak.config(height=2, width = 34)
        przycisk_atak.grid(column=0, row=1)

        rama.place(relx=0.65, rely=0.79)




'''
Funkcje do pobierania eq
'''

def polaczenie():
        baza = sqlite3.connect('dane.db')
        return baza

'''
Działanie programu
'''
okno = Tk()
okno.geometry('960x640')
gracz = jednostka('gracz',gracz=True)
przeciwnik = jednostka('kot')

def odswiez(obiekt, okno=okno, gracz=gracz, przeciwnik=przeciwnik):
    obiekt.destroy()
    obiekt = Walka(okno, gracz, przeciwnik)
    obiekt.place(relwidth=1,relheight=1)

rama = Walka(okno, gracz, przeciwnik)
rama.place(relwidth=1,relheight=1)
okno.bind('<BackSpace>', lambda x: odswiez(rama))
okno.mainloop()