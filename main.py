import urllib.request
from tkinterhtml import HtmlFrame
from tkinter import *
import tkinter as tk

root = tk.Tk()

label=Label(root, text="Pekan selain", font=("Courier 22 bold"))
label.pack()


entry= Entry(root, width= 40)
entry.focus_set()
entry.pack()
frame = HtmlFrame(root, horizontal_scrollbar="auto")

def internet():
    global entry
    global frame
    string= entry.get()
    frame.destroy()
    frame = HtmlFrame(root, horizontal_scrollbar="auto")
    frame.set_content("<html></html>")
    frame.set_content(urllib.request.urlopen(string).read().decode())
    frame.pack()

tk.Button(root, text= "Avaa", width= 20, command = internet).pack(pady=20)



root.mainloop()