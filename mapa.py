import random
import sqlite3
from os import system
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk

root = Tk()
root.geometry('700x650')

global mapa_foty, mapa_znaczniki
nazwyplikow = [[y+'.png',y+'_b.png',y+'_c.png'] for y in ['mapa_obrazy\\pole_pus','mapa_obrazy\\pole_krzak','mapa_obrazy\\pole_woda']]
mapa_foty = []
for i in nazwyplikow:
    mapa_foty.append([ImageTk.PhotoImage(master=root, file=x) for x in i])

class Pole():
    def __init__(self):
        ####
        # Tworzy pole
        ####
        if random.randint(0,100)%11==0:
            self.interakcja = True
        else:
            self.interakcja = False 
        self.rodzaj=random.randrange(0,3)

    def obraz(self, pole):
        ####
        # Funkcja pozwala na zwracanie wizualnej reprezentacji pola
        ####
        if pole[0]==4 and pole[1]==4:
            czy=1
        elif self.zwrocinter()==True:
            czy=2
        else:
            czy=0
        obrazek = mapa_foty[self.zwrocrodzaj()][czy]
        return obrazek

    def zwrocrodzaj(self):
        return self.rodzaj
    
    def zwrocinter(self):
        return self.interakcja

class Mapa():
    def __init__(self):
        ####
        # Generuje instancję mapy
        ####
        self.gracz_x = 51
        self.gracz_y = 51
        self.mapa = self.mapgen()

    ### Funkcje ruszania ###
    def ruch(self, koordynaty, operacja):
        koordynaty+=1*operacja
        if koordynaty+3>=len(self.mapa) or koordynaty-3<=0:
            koordynaty-=1*operacja
            messagebox.showwarning(title='Zły ruch', message='Doszedłeś tam, gdzie nawet dźwięk Bajmu nie dociera, wybierz inny ruch')
        return koordynaty
    def ruch_prawo(self):
        self.gracz_x=self.ruch(self.gracz_x, 1)
        self.akcja()
        self.calosc.event_generate('<BackSpace>')
    def ruch_lewo(self):
        self.gracz_x=self.ruch(self.gracz_x, -1)
        self.akcja()
        self.calosc.event_generate('<BackSpace>')
    def ruch_dol(self):
        self.gracz_y=self.ruch(self.gracz_y, 1)
        self.akcja()
        self.calosc.event_generate('<BackSpace>')
    def ruch_gora(self):    
        self.gracz_y=self.ruch(self.gracz_y, -1)
        self.akcja()
        self.calosc.event_generate('<BackSpace>')

    def akcja(self):
        ####
        # Funkcja uruchamiana przy nastąpieniu na pole z interakcją
        ####
        if self.mapa[self.gracz_y][self.gracz_x].zwrocinter()==True:
            if random.randrange(0,3)==0:
                # Rozpoczynanie walki
                system('python walka.py')
            else:
                # Dodawanie przedmiotów do eq
                baza = polaczenie()
                kursor = baza.cursor()
                kursor.execute('INSERT INTO bajm_eq (utwor) SELECT DISTINCT utwor FROM bajm ORDER BY RANDOM() LIMIT 1')
                baza.commit()
                baza.close()
                messagebox.showinfo(title='Zdobyto nowy utwór!', message='Zdobyłeś nowy utwór, sprawdź swoje eq w trakcie walki!')
            self.mapa[self.gracz_y][self.gracz_x].interakcja=False
    def render(self, okno):
        ####
        # Generuje okno z mapą
        ####
        self.calosc=Frame(okno)

        # Generowanie podglądu mapy
        self.rysunekmapy=Frame(self.calosc)
        i_region = 0
        for i in range(self.zwrocgracz()[1]-3,self.zwrocgracz()[1]+4):
            i_region +=1
            j_region = 0
            for j in range(self.zwrocgracz()[0]-3,self.zwrocgracz()[0]+4):
                j_region += 1
                Label(master=self.rysunekmapy, image=self.mapa[i][j].obraz([i_region,j_region])).grid(row=i_region, column=j_region)
        # Generowanie reszty UI
        self.przyciskgora = Button(master=self.calosc, text='W górę', command=self.ruch_gora)
        self.przyciskgora.pack(side=TOP)
        self.przyciskprawo = Button(master=self.calosc, text='Prawo', command=self.ruch_prawo)
        self.przyciskprawo.pack(side=RIGHT)
        self.przycisklewo = Button(master=self.calosc, text='Lewo', command=self.ruch_lewo)
        self.przycisklewo.pack(side=LEFT)
        self.przyciskdol = Button(master=self.calosc, text='W dół', command=self.ruch_dol)
        self.przyciskdol.pack(side=BOTTOM)
        self.rysunekmapy.pack()
        self.calosc.place(relwidth=1,relheight=1)

    def mapgen(self):
        ####
        # Zwraca losowo wygenerowaną mapę w formie tablicy dwuwymiarowej
        ####
        wielkosc = 101 # Wartość do konfiguracji
        mapa = []
        for i in range(wielkosc):
            linia = []
            for j in range(wielkosc):
                linia.append(Pole())
            mapa.append(linia)
        return mapa

    def zwrocgracz(self):
        return [self.gracz_x, self.gracz_y]

def polaczenie():
    ####
    # Funkcja generuje połączenie do bazy danych
    ####
    baza = sqlite3.connect('dane.db')
    return baza

def odswiez(obiekt, okno=root):
        ####
        # Funkcja służy do odświeżania interfejsu
        ####
        obiekt.calosc.destroy()
        obiekt.render(root)

mapa = Mapa()
mapa.render(root)
root.bind('<BackSpace>', lambda x: odswiez(mapa))

root.mainloop()