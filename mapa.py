from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

root = Tk()

canvas = Canvas(root, width=800, height=800)
canvas.pack()

#przykładowe tło
obraz_tlo=Image.open("różowy.jpg")
obrazTk_tlo=ImageTk.PhotoImage(obraz_tlo)

#seria roboczych, losowo się układających obiektów
obraz1=Image.open("czarny.jpg")
obrazTk1=ImageTk.PhotoImage(obraz1)
wysokosc1=random.randrange(24)*20+20
szerokosc1=random.randrange(24)*20+20

obrazTk2=ImageTk.PhotoImage(obraz1)
wysokosc2=random.randrange(24)*20+20
szerokosc2=random.randrange(24)*20+20

obrazTk3=ImageTk.PhotoImage(obraz1)
wysokosc3=random.randrange(24)*20+20
szerokosc3=random.randrange(24)*20+20

obrazTk4=ImageTk.PhotoImage(obraz1)
wysokosc4=random.randrange(24)*20+20
szerokosc4=random.randrange(24)*20+20

#obiekt kontrolowany przez użytkownika
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

#kod umożliwiający poruszanie, blokuje możliwość wyjścia poza tło
def move(event):
    global x1, y1, szerokosc_moving, wysokosc_moving
    if event.char == "a" and szerokosc_moving > 20:
        canvas.move(image, -20, 0)
        szerokosc_moving-=20
    elif event.char == "d" and szerokosc_moving < 480:
        canvas.move(image, 20, 0)
        szerokosc_moving+=20
    elif event.char == "w" and wysokosc_moving > 20:
        canvas.move(image, 0, -20)
        wysokosc_moving-=20
    elif event.char == "s" and wysokosc_moving < 480:
        canvas.move(image, 0, 20)
        wysokosc_moving+=20

#funkcja sprawdzająca lokalizację poruszanego obiektu
def lokalizacja():
    messagebox.showinfo(szerokosc_moving,wysokosc_moving)

#funkcja za pomocą której sprawdza się, czy poruszany obiekt pokrywa
#się z którymś z innych obiektów
def sprawdz_nalozenie():
    global szerokosc_moving, wysokosc_moving, szerokosc4, wysokosc4, szerokosc3, wysokosc3, szerokosc2, wysokosc2, szerokosc1, wysokosc1
    if szerokosc_moving == szerokosc1 and wysokosc_moving == wysokosc1:
        messagebox.showinfo("Nałożenie","Potwierdzone")
    elif szerokosc_moving == szerokosc2 and wysokosc_moving == wysokosc2:
        messagebox.showinfo("Nałożenie","Potwierdzone")
    elif szerokosc_moving == szerokosc3 and wysokosc_moving == wysokosc3:
        messagebox.showinfo("Nałożenie","Potwierdzone")
    elif szerokosc_moving == szerokosc4 and wysokosc_moving == wysokosc4:
        messagebox.showinfo("Nałożenie","Potwierdzone")
    else:
        messagebox.showinfo("Nałożenia","Nie ma")

przycisk_lokalizacja=Button(root,text="lokalizacja",command=lokalizacja)
przycisk_lokalizacja.place(y=300,x=700)

przycisk_nalozenie=Button(root,text="nałożenie",command=sprawdz_nalozenie)
przycisk_nalozenie.place(y=250,x=700)

root.bind("<Key>", move)
root.mainloop()
