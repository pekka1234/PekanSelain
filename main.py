import urllib.request
from tkinterhtml import HtmlFrame
from tkinter import *
import tkinter as tk

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

# Yhdistää internettiin ja näyttää renderöidyn html:n
def internet():
    # Tarvitaan osoitekentän syöte ja yhtys htmlframeen
    global entry
    global frame
    # Osoitteen hakeminen
    string= entry.get()
    # Poistetaan aikaisempi sivu
    frame.destroy()
    # Uuden sivun luonti ja internettiin yhdistäminen sivun html:n hakemista varten
    frame = HtmlFrame(root, horizontal_scrollbar="auto")
    frame.set_content("<html></html>")
    frame.set_content(urllib.request.urlopen(string).read().decode())
    frame.pack()

# Avaa nappi, joka suorittaa internet funktion
tk.Button(root, text= "Avaa", width= 20, command = internet).pack(pady=20)

# Avataan ikkuna
root.mainloop()