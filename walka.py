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
    def __init__(self, gracz=False):
        self.hp=IntVar()
        if gracz==True:
            self.hp.set(400)
            fota=Image.open('bohater.jpg')
            self.imie="Biały żołnierz"
        else:
            self.hp.set(100)
            baza=polaczenie()
            kursor = baza.cursor()
            kursor.execute('SELECT DISTINCT utwor FROM przeciwnik ORDER BY RANDOM()')
            self.imie=kursor.fetchone()[0]
            fota=Image.open('przeciwnik.png')
            baza.close()
        fota=fota.resize((250,250),Image.ANTIALIAS)
        self.obraz=ImageTk.PhotoImage(image=fota)

    def zwrochp(self):
        return str(self.hp.get())
    
    def zwrocobraz(self):
        return self.obraz
    
    def zwrocimie(self):
        return self.imie

class Walka(Frame):

    def dokoncz_ture(self):
        ####
        # Funkcja wykonywana pod zakończenie każdej akcji gracza.
        # Aktualizuje UI oraz sprawdza poziom życia.
        ####
        #Tura przeciwnika
        baza = polaczenie()
        kursor = baza.cursor()
        kursor.execute("SELECT * FROM przeciwnik WHERE utwor = (?) ORDER BY RANDOM()",[self.przeciwnik.zwrocimie()])
        wynik = kursor.fetchone()[0]
        baza.close()
        sila = len(wynik)
        self.gracz.hp.set(self.gracz.hp.get()-sila)
        messagebox.showinfo(title="Wynik ataku", message="Przeciwnik wykorzystuje linię: \""+wynik+"\"\nOtrzymałeś "+str(sila)+" punktów obrażeń.\nZostało Ci "+self.gracz.zwrochp()+" HP.")
        #Sprawdzenie poziomu życia
        if self.gracz.hp.get()<=0:
            messagebox.showwarning(message="Przegrałeś pojedynek!")
            self.quit()
        elif self.przeciwnik.hp.get()<=0:
            messagebox.showwarning(message="Wygrałeś pojedynek!")
            self.quit()
        #Odświeżenie ekranu
        self.event_generate('<BackSpace>')

    def atakuj(self):
        ####
        # Funkcja wykonywana przy naciśnięciu przycisku "Atakuj"
        ####
        czym = self.wybrana.get()
        assert czym!="Wybierz broń","Nie wybrano broni"
        baza = polaczenie()
        kursor = baza.cursor()
        kursor.execute("SELECT * FROM bajm WHERE utwor = (?) ORDER BY RANDOM()",[czym])
        wynik = kursor.fetchone()[0]
        baza.close()
        sila=len(wynik)
        self.przeciwnik.hp.set(self.przeciwnik.hp.get()-sila)
        messagebox.showinfo(title="Wynik ataku", message="Wykorzystujesz linię: \""+wynik+"\"\nPrzeciwnik otrzymał "+str(sila)+" punktów obrażeń.\nZostało mu "+self.przeciwnik.zwrochp()+" HP.")
        self.dokoncz_ture()

    def lecz(self):
        ####
        # Funkcja wykonywana przy wciśnięciu przycisku "Wylecz się"
        ####
        self.gracz.hp.set(self.gracz.hp.get()+50)
        messagebox.showinfo(title="Leczenie", message="Otrzymujesz 50 HP, masz teraz łącznie "+self.gracz.zwrochp()+" HP.")
        self.dokoncz_ture()

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
        przycisk_omin = Button(rama, text="Pomiń turę", command=self.dokoncz_ture)
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
        opcje = zbierz()
        self.wybrana = StringVar(self, 'Wybierz broń')
        polewyboru = OptionMenu(rama, self.wybrana, 'Wybierz broń', *opcje)
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
    ####
    # Funkcja generuje połączenie do bazy danych
    ####
    baza = sqlite3.connect('dane.db')
    return baza

def zbierz():
    ####
    # Tworzy listę dostępnych utworów (DO POPRAWY PO STWORZENIU MAPY - dodać to tabeli dodatkowe kolumny)
    ####
    baza = polaczenie()
    kursor = baza.cursor()
    kursor.execute('SELECT DISTINCT utwor FROM bajm_eq')
    wynik = kursor.fetchall()
    baza.close()
    return [i[0] for i in wynik] #zwraca listę utworów, zamiast listy singletonów z utworami


'''
Działanie programu
'''
okno = Tk()
okno.geometry('960x640')
gracz = jednostka(gracz=True)
przeciwnik = jednostka()

def odswiez(obiekt, okno=okno, gracz=gracz, przeciwnik=przeciwnik):
        ####
        # Funkcja służy do odświeżania interfejsu
        ####
        obiekt.destroy()
        obiekt = Walka(okno, gracz, przeciwnik)
        obiekt.place(relwidth=1,relheight=1)

rama = Walka(okno, gracz, przeciwnik)
rama.place(relwidth=1,relheight=1)
okno.bind('<BackSpace>', lambda x: odswiez(rama))
okno.mainloop()