import urllib.request
from tkinterhtml import HtmlFrame
from tkinter import *
import tkinter as tk
from bs4 import BeautifulSoup

# Ikkunan luonti
root = tk.Tk()

# Otsikko
label = Label(root, text="Pekan selain", font=("Courier 22 bold"))
label.pack()

# Osoitteen syöttökenttä
entry= Entry(root, width= 40)
entry.focus_set()
entry.pack()

# HtmlFramen luonti, jotta se olisi globaali ja voitaisiin käyttää funktiossa niin, että viitataan aikaisemmin suoritettuun funktioon, jotta aikaisempi sivu voidaan poistaa toisen tieltä
frame = HtmlFrame(root, horizontal_scrollbar="auto")
lf = HtmlFrame(root, horizontal_scrollbar="auto")

# Yhdistää internettiin ja näyttää renderöidyn html:n
def internet():
    # Tarvitaan osoitekentän syöte ja yhtys htmlframeen
    global entry
    global frame
    global lf
    # Osoitteen hakeminen
    string= entry.get()
    # Poistetaan aikaisempi sivu
    frame.destroy()
    # Uuden sivun luonti ja internettiin yhdistäminen sivun html:n hakemista varten
    frame = HtmlFrame(root, horizontal_scrollbar="auto")
    frame.set_content("<html></html>")
    # Tätä muuttujaa voidaan käyttää myös linkkien saamisessa
    html = urllib.request.urlopen(string).read()
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
        thtml += "        <h1>" + x + "</h1>\n"
    thtml += "    </body>\n</html>"    
    # Poistetaan aikaisempi sivu
    lf.destroy()
    # Lisätään linkki html sivu
    lf = HtmlFrame(root, horizontal_scrollbar="auto")
    lf.set_content("<html></html>")
    lf.set_content(thtml)
    lf.pack()      
        


# Avaa nappi, joka suorittaa internet funktion
tk.Button(root, text= "Avaa", width= 20, command = internet).pack(pady=20)

# Avataan ikkuna
root.mainloop()