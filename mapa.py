from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
from os import system
import sqlite3

root = Tk()

global mapa_foty
mapa_foty = [Image.open(x) for x in ['pole_pus.png','pole_krzak.png','pole_woda.png']]

class Pole():
    def __init__(self):
        if random.randint(0,100)%11==0:
            self.interakcja = True
        else:
            self.interakcja = False 
        
        self.rodzaj=random.randrange(0,3)

    def __repr__(self):
        return mapa_foty[self.zwrocrodzaj]

    def zwrocrodzaj(self):
        return self.rodzaj
    
    def zwrocinter(self):
        return self.interakcja

canvas = Canvas(root, width=800, height=800)
canvas.pack()

class Mapa(Frame):
    def render(self):
        

    def __init__(self, poz):
        self.gracz_x = poz[0]
        self.gracz_y = poz[1]


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

root.mainloop()
'''