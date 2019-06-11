from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
from os import system

root = Tk()

canvas = Canvas(root, width=800, height=800)
canvas.pack()

#męskie różowe tło
obraz_tlo=Image.open("różowy.jpg")
obrazTk_tlo=ImageTk.PhotoImage(obraz_tlo)

#seria losowo rozłożonych czarnych obiektów symulujących przeciwników
obraz1=Image.open("czarny.jpg")
obrazTk1=ImageTk.PhotoImage(obraz1)
wysokosc1=random.randrange(24)*20+20
szerokosc1=random.randrange(24)*20+20
status1 = 1 #stan aktywności obiektu

obrazTk2=ImageTk.PhotoImage(obraz1)
wysokosc2=random.randrange(24)*20+20
szerokosc2=random.randrange(24)*20+20
status2 = 1

obrazTk3=ImageTk.PhotoImage(obraz1)
wysokosc3=random.randrange(24)*20+20
szerokosc3=random.randrange(24)*20+20
status3 = 1

obrazTk4=ImageTk.PhotoImage(obraz1)
wysokosc4=random.randrange(24)*20+20
szerokosc4=random.randrange(24)*20+20
status4 = 1

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
def popup():
    global szerokosc_moving, wysokosc_moving, szerokosc4, wysokosc4, szerokosc3, wysokosc3, szerokosc2, wysokosc2, szerokosc1, wysokosc1, status1, status2, status3, status4    
    system('python walka.py')
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
