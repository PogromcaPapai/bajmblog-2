from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()

canvas = Canvas(root, width=800, height=800)
canvas.pack()

#tło

obraz1=Image.open("różowy.jpg")
obrazTk1=ImageTk.PhotoImage(obraz1)

#Dalej idzie seria czarnych kwadracików. Powinienem był zrobić to ładniej, ale to później.
#Wyszczególniłem wartości x i y, bo mogą się przydać do definiowania interakcji z przeciwnikami.

obraz2=Image.open("czarny.jpg")
obrazTk2=ImageTk.PhotoImage(obraz2)
y2=random.randrange(24)
wysokosc2=y2*20+20
x2=random.randrange(24)
szerokosc2=x2*20+20

obraz3=Image.open("czarny.jpg")
obrazTk3=ImageTk.PhotoImage(obraz3)
y3=random.randrange(24)
wysokosc3=y3*20+20
x3=random.randrange(24)
szerokosc3=x3*20+20

obraz4=Image.open("czarny.jpg")
obrazTk4=ImageTk.PhotoImage(obraz4)
y4=random.randrange(24)
wysokosc4=y4*20+20
x4=random.randrange(24)
szerokosc4=x4*20+20

obraz5=Image.open("czarny.jpg")
obrazTk5=ImageTk.PhotoImage(obraz5)
y5=random.randrange(24)
wysokosc5=y5*20+20
x5=random.randrange(24)
szerokosc5=x5*20+20

#kontrolowany przez użytkownika biały kwadracik

obraz6=Image.open("biały.jpg")
obrazTk6=ImageTk.PhotoImage(obraz6)
y6=1
wysokosc6=y6*20
x6=1
szerokosc6=x6*20

canvas=Canvas(root,width=1000,height=1000)
canvas.place(y=100,x=0)
canvas.create_image(0,0,image=obrazTk1)
canvas.create_image(wysokosc2,szerokosc2,image=obrazTk2)
canvas.create_image(wysokosc3,szerokosc3,image=obrazTk3)
canvas.create_image(wysokosc4,szerokosc4,image=obrazTk4)
canvas.create_image(wysokosc5,szerokosc5,image=obrazTk5)
image = canvas.create_image(wysokosc6,szerokosc6,image=obrazTk6)

#kod umożliwiający poruszanie kwadracikiem 

def move(event):
    global x1, y1
    if event.char == "a":
        canvas.move(image, -20, 0)
    elif event.char == "d":
        canvas.move(image, 20, 0)
    elif event.char == "w":
        canvas.move(image, 0, -20)
    elif event.char == "s":
        canvas.move(image, 0, 20)

root.bind("<Key>", move)

root.mainloop()
