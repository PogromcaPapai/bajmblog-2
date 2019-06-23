import random
import sqlite3
from os import system
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk

root = Tk()

global mapa_foty, mapa_znaczniki
nazwyplikow = [[y+'.png',y+'_b.png',y+'_c.png'] for y in ['mapa_obrazy\\pole_pus','mapa_obrazy\\pole_krzak','mapa_obrazy\\pole_woda']]
mapa_foty = []
for i in nazwyplikow:
    mapa_foty.append([ImageTk.PhotoImage(master=root, file=x) for x in i])

class Pole():
    def __init__(self):
        if random.randint(0,100)%11==0:
            self.interakcja = True
        else:
            self.interakcja = False 
        self.rodzaj=random.randrange(0,3)

    def obraz(self, pole):
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
        self.gracz_x = 3
        self.gracz_y = 3
        self.mapa = self.mapgen()

    def odswiez(self, okno):
        self.rysunekmapy.destroy()
        self.render(okno)

    def render(self, okno):
        self.rysunekmapy=Frame(okno)
        i_region = 0
        for i in range(self.zwrocgracz()[1]-3,self.zwrocgracz()[1]+4):
            i_region +=1
            j_region = 0
            for j in range(self.zwrocgracz()[0]-3,self.zwrocgracz()[0]+4):
                j_region += 1
                Label(master=self.rysunekmapy, image=self.mapa[i][j].obraz([i_region,j_region])).grid(row=i_region, column=j_region)
        self.rysunekmapy.pack()

    def mapgen(self):
        wielkosc = 17
        mapa = []
        for i in range(wielkosc):
            linia = []
            for j in range(wielkosc):
                linia.append(Pole())
            mapa.append(linia)
        return mapa

    def zwrocgracz(self):
        return [self.gracz_x, self.gracz_y]

mapa = Mapa()
mapa.render(root)

root.mainloop()
'''
#bialy obiekt sterowany wsadem przez użytkownika
obraz_moving=Image.open("biały.jpg")
obrazTk_moving=ImageTk.PhotoImage(obraz_moving)
wysokosc_moving=20
szerokosc_moving=20

canvas=Canvas(root,width=1000,height=1000)
canvas.place(y=100,x=0)
canvas.create_image(0,0,image=obrazTk_tlo)
canvas.create_image(szerokosc1,wysokosc1,image=obrazTk1)
canvas.create_image(szerokosc2,wysokosc2,image=obrazTk2)
canvas.create_image(szerokosc3,wysokosc3,image=obrazTk3)
canvas.create_image(szerokosc4,wysokosc4,image=obrazTk4)
image = canvas.create_image(szerokosc_moving,wysokosc_moving,image=obrazTk_moving)

#okno z miejscem na walkę
def polaczenie():
    ####
    # Funkcja generuje połączenie do bazy danych
    ####
    baza = sqlite3.connect('dane.db')
    return baza

def popup():
    global szerokosc_moving, wysokosc_moving, szerokosc4, wysokosc4, szerokosc3, wysokosc3, szerokosc2, wysokosc2, szerokosc1, wysokosc1, status1, status2, status3, status4    
    if random.randrange(0,3)==0:
        system('python walka.py')
    else:
        baza = polaczenie()
        kursor = baza.cursor()
        kursor.execute('INSERT INTO bajm_eq (utwor) SELECT DISTINCT utwor FROM bajm ORDER BY RANDOM() LIMIT 1')
        baza.commit()
        baza.close()
        messagebox.showinfo(title='Zdobyto nowy utwór!', message='Zdobyłeś nowy utwór, sprawdź swoje eq w trakcie walki!')
    if szerokosc_moving == szerokosc1 and wysokosc_moving == wysokosc1 and status1 == 1:
        status1 -= 1 #dezaktywacja obiektu
    elif szerokosc_moving == szerokosc2 and wysokosc_moving == wysokosc2 and status2 == 1:
        status2 -= 1
    elif szerokosc_moving == szerokosc3 and wysokosc_moving == wysokosc3 and status3 == 1:
        status3 -= 1
    elif szerokosc_moving == szerokosc4 and wysokosc_moving == wysokosc4 and status4 == 1:
        status4 -= 1

#funkcja sprawdzająca położenie i aktywnośc obiektu    
def sprawdz_polozenie():
    global szerokosc_moving, wysokosc_moving, szerokosc4, wysokosc4, szerokosc3, wysokosc3, szerokosc2, wysokosc2, szerokosc1, wysokosc1, status1, status2, status3, status4
    if szerokosc_moving == szerokosc1 and wysokosc_moving == wysokosc1 and status1 == 1:
        popup()
    elif szerokosc_moving == szerokosc2 and wysokosc_moving == wysokosc2 and status2 == 1:
        popup()
    elif szerokosc_moving == szerokosc3 and wysokosc_moving == wysokosc3 and status3 == 1:
        popup()
    elif szerokosc_moving == szerokosc4 and wysokosc_moving == wysokosc4 and status4 == 1:
        popup()

#funkcja ruchu z ciągłą weryfikacją położenia        
def move(event):
    global x1, y1, szerokosc_moving, wysokosc_moving
    if event.char == "a" and szerokosc_moving > 20:
        canvas.move(image, -20, 0)
        szerokosc_moving-=20
        sprawdz_polozenie()
    elif event.char == "d" and szerokosc_moving < 480:
        canvas.move(image, 20, 0)
        szerokosc_moving+=20
        sprawdz_polozenie()
    elif event.char == "w" and wysokosc_moving > 20:
        canvas.move(image, 0, -20)
        wysokosc_moving-=20
        sprawdz_polozenie()
    elif event.char == "s" and wysokosc_moving < 480:
        canvas.move(image, 0, 20)
        wysokosc_moving+=20
        sprawdz_polozenie()

root.bind("<Key>", move)

#robocza funkcja ułatwiająca mierzenie mapy
def lokalizacja():
    messagebox.showinfo(szerokosc_moving,wysokosc_moving)

przycisk_lokalizacja=Button(root,text="lokalizacja",command=lokalizacja)
przycisk_lokalizacja.place(y=300,x=700)
'''
