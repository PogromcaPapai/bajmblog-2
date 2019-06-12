#se robie menu narazie brzydkie i tylko trzy przyciski ale do przodu czy cos 

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from bs4 import BeautifulSoup
import sqlite3

#baza danych 2.0

def polaczenie():
        baza = sqlite3.connect('dane.db')
        return baza

def usuwajzle(zwrot):
        ####
        # Usuwa niepożądane znaki/zwroty
        ####
        listazlych=['<br/>','div class="txt border">','</div','<','>','\n','\r','                    ','div class="song-text"','h2Tekst piosenki:/h2'
]
        for i in listazlych:
                zwrot = zwrot.replace(i, '')
        return zwrot

def dodaj(kursor, tresc, zespol):
        if len(tresc[0])<=400 and len(tresc[0])>5:
                kursor.execute('INSERT INTO '+zespol+' VALUES (?,?,?)', tresc)

#funkcje przycisków czyli pierwsza wersja ale na sterydach xD

def autorzy():
    messagebox.showinfo("Twórcy tego cuda","Jakub Dakowski\nNatalia Majda\nWojciech Zięba")
def zacznij_gierke():
    messagebox.showinfo("Rozpocznij gierkę","Za-za-zaczynajmy!")
def baza_bajm():
    messagebox.showinfo("Aktualizacja danych","Rozpoczęło się pobieranie utworów Bajmu")
    baza = polaczenie()
    baza.execute('DROP TABLE IF EXISTS bajm')
    baza.execute('DROP TABLE IF EXISTS bajm_eq'
    kursor = baza.cursor()
    kursor.execute('CREATE TABLE bajm (tresc text, utwor text)')
    kursor.execute('CREATE TABLE bajm_eq (utwor text)')
    print('Baza utworzona')
    listaglowna = []
    adres = 'https://www.tekstowo.pl/piosenki_artysty,bajm'
    n=0
    while True:
        n+=1
        strona = requests.get(adres)
        drzewunio=BeautifulSoup(strona.content, 'lxml')
        print("Rozpoczynam przeszukiwanie strony",n)
        listazaznaczen = drzewunio.find('div', class_ = 'ranking-lista').find_all('a', class_ = 'title')
        nastepna = drzewunio.find('div', class_='padding').find_all('a', title='Następna >>')
        listaglowna.extend(listazaznaczen)
        if nastepna!=[]:
            adres = "https://www.tekstowo.pl"+nastepna[0]['href']
        else:
            break
    listalinkow=dict()
    for i in listaglowna:
        # pobieranie tekstów #
        listalinkow[i.string]='https://www.tekstowo.pl'+i['href']
    print("Zakończono zbieranie linków")
    for i in listalinkow:
        # upload linii #
        print("Pobieranie tekstu",i)
        stronka=requests.get(listalinkow[i])
        wybrana_tekst = BeautifulSoup(stronka.content, 'lxml').find('div', class_='song-text')
        lista = str(wybrana_tekst).splitlines()
        for j in lista:
            tekst=usuwajzle(str(j))
            dodaj(baza, (tekst, i, 0), 'bajm')
    baza.commit()
    baza.close()
def baza_przeciwnik():
    messagebox.showinfo("Aktualizacja danych","Rozpoczęło się pobieranie utworów przeciwnika")
    baza = polaczenie()
    baza.execute('DROP TABLE IF EXISTS przeciwnik')
    kursor = baza.cursor()
    kursor.execute('CREATE TABLE przeciwnik (tresc text, utwor text)')
    print('Baza utworzona')
    listaglowna = []
    adres = zespol.get()
    n=0
    while True:
        n+=1
        strona = requests.get(adres)
        drzewunio=BeautifulSoup(strona.content, 'lxml')
        print("Rozpoczynam przeszukiwanie strony",n)
        listazaznaczen = drzewunio.find('div', class_ = 'ranking-lista').find_all('a', class_ = 'title')
        nastepna = drzewunio.find('div', class_='padding').find_all('a', title='Następna >>')
        listaglowna.extend(listazaznaczen)
        if nastepna!=[]:
            adres = "https://www.tekstowo.pl"+nastepna[0]['href']
        else:
            break
    listalinkow=dict()
    for i in listaglowna:
        # pobieranie tekstów #
        listalinkow[i.string]='https://www.tekstowo.pl'+i['href']
    print("Zakończono zbieranie linków")
    for i in listalinkow:
        # upload linii #
        print("Pobieranie tekstu",i)
        stronka=requests.get(listalinkow[i])
        wybrana_tekst = BeautifulSoup(stronka.content, 'lxml').find('div', class_='song-text')
        lista = str(wybrana_tekst).splitlines()
        for j in lista:
            tekst=usuwajzle(str(j))
            dodaj(baza, (tekst, i, 0), 'przeciwnik')
    baza.commit()
    baza.close()
def baza_both():
    baza_bajm()
    baza_przeciwnik()


glowneOkno=Tk()

pasekMenu=Menu(glowneOkno)
pierwszeMenu=Menu(pasekMenu,tearoff=0)

pierwszeMenu.add_command(label="Zaktualizuj bazę cytatów",command=baza_both)
pierwszeMenu.add_command(label="Zamknij",command=glowneOkno.quit)
pasekMenu.add_cascade(label="Opcje",menu=pierwszeMenu)

pomocMenu=Menu(pasekMenu,tearoff=0)
pomocMenu.add_command(label="O Autorach",command=autorzy)
pasekMenu.add_cascade(label="Autorzy",menu=pomocMenu)

#daje logo i kocham śledzie

logo_canvas= Canvas(glowneOkno,width=500,height=150)
logo_canvas.pack()
#logo_pliczek=ImageTk.PhotoImage(Image.open('logo.gif'))
#logo_canvas.create_image(250,60,image=logo_pliczek)

przycisk_rozpoczecie=Button(glowneOkno,text="Rozpocznij grę!",command=zacznij_gierke)
przycisk_rozpoczecie.pack()

zespol = StringVar(glowneOkno, value="https://www.tekstowo.pl/piosenki_artysty,golec_uorkiestra")
zmiana_zespolu_tekst=Label(glowneOkno, text="\nPodaj adres do strony tekstowo.pl wybranego zespołu:")
zmiana_zespolu_tekst.pack()
zmiana_zespolu=Entry(glowneOkno, textvariable=zespol, width=40)
zmiana_zespolu.pack()
zmiana_zespolu_przycisk=Button(glowneOkno, text="Zmień przeciwnika!", command=baza_przeciwnik)
zmiana_zespolu_przycisk.pack()

glowneOkno.config(menu=pasekMenu)
glowneOkno.geometry('960x640')

glowneOkno.mainloop()
