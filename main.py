import urllib.request
from tkinterhtml import HtmlFrame
from tkinter import *
import tkinter as tk
from bs4 import BeautifulSoup

# Edellisen sivun vaihto
es = []
k = 0

# Ikkunan luonti
root = tk.Tk()

# Otsikko
label = Label(root, text="Pekan selain", font=("Courier 22 bold"))
label.pack()

# Osoitteen syöttökenttä
entry = Entry(root, width= 40)
entry.focus_set()
entry.pack()

# HtmlFramen luonti, jotta se olisi globaali ja voitaisiin käyttää funktiossa niin, että viitataan aikaisemmin suoritettuun funktioon, jotta aikaisempi sivu voidaan poistaa toisen tieltä
frame = HtmlFrame(root, horizontal_scrollbar="auto")
lf = HtmlFrame(root, horizontal_scrollbar="auto")

# Yhdistää internettiin ja näyttää renderöidyn html:n
def internet(kw):
    # Tarvitaan osoitekentän syöte ja yhtys htmlframeen
    global entry
    global frame
    global lf
    global k
    # Osoitteen hakeminen
    string = entry.get()
    # Poistetaan aikaisempi sivu
    frame.destroy()
    # Uuden sivun luonti ja internettiin yhdistäminen sivun html:n hakemista varten
    frame = HtmlFrame(root, horizontal_scrollbar="auto")
    frame.set_content("<html></html>")
    # Tätä muuttujaa voidaan käyttää myös linkkien saamisessa
    try:
        html = urllib.request.urlopen(string).read()
        # Jutut sivun vaihdosta varten (siis siinä on käytännössä sivu lista missä mennään edestakas)
        if kw:
            if string not in es:
                es.append(string)
                k = len(es) - 1
    except:
        html = ""    
    frame.set_content(html.decode())
    frame.pack()
    # Koko seuraava osio on: Linkkien haku, eli etsitään beaoutiful soupin avulla kaikki linkit, joita sivulla on jotta pääsee kunnolla surffaamaaan verkossa kopiomalla sivun sisällä olevan linkin ja liittämällä sen kenttään ja painamalla avaa
    hrefs = []
    thtml = "<!DOCTYPE html>\n<html>\n    <body>\n"
    soup = BeautifulSoup(html, 'lxml')
    for a in soup.find_all('a', href=True):
        hrefs.append(a['href'])
    #print(hrefs)
    for x in hrefs:
        thtml += "        <h2>" + x + "</h2>\n"
    thtml += "    </body>\n</html>"    
    # Poistetaan aikaisempi sivu
    lf.destroy()
    # Lisätään linkki html sivu
    lf = HtmlFrame(root, horizontal_scrollbar="auto")
    lf.set_content("<html></html>")
    lf.set_content(thtml)
    lf.pack()      
        
# Mennään edellieen
def sw():
    global es, k
    if k - 1 >= 0:
        k -= 1
        entry.delete(0, END)
        print(es, k)
        entry.insert(0, es[k])
        internet(False)

# Mennään "tulevaan"
def swt():
    global es, k
    if k + 1 < len(es):
        k += 1
        entry.delete(0, END)
        entry.insert(0, es[k]) 
        internet(True)       

# Ei voi pistää arvoja suoraan command =, kautta
def inter():
    internet(True)

# Avaa nappi, joka suorittaa internet funktion
tk.Button(root, text= "Avaa", width= 20, command = inter).pack(pady=20)

# Napit sivuun palaamiseen
tk.Button(root, text= "←", width= 2, font=("Helvetica 22 bold"), command = sw).pack(side=LEFT, padx=50)
tk.Button(root, text= "→", width= 2, font=("Helvetica 22 bold"), command = swt).pack(side=RIGHT, padx=50)

# Avataan ikkuna
root.mainloop()