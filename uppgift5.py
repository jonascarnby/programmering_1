# -* coding UTF-8 -*-

"""
Jonas Carnby
Python Ver 3.4.1
OSX 10.9.5
Uppgift 5
"""

#importerar Tkinter
import sys
from tkinter import *
import tkinter.messagebox
import JonasCarnbyUppgift3py3.4.1 as paliCheck

paliCheck.check

mGui = Tk()
mGui.geometry("800x300+300+300")
topFrame = Frame(mGui)
topFrame.pack()
midFrame = Frame(mGui)
midFrame.pack()
bottomFrame = Frame(mGui)
bottomFrame.pack()
bottomFrame.config(width="300")

mGui.title("Palindrome?")

topLabel = Label(topFrame, text = "Skriv in texten du vill kontrollera: ")
topLabel.pack(side="left")
uInput = Entry(topFrame, textvariable = ment)
uInput.pack(side="left")
kontrollera_knapp = Button (topFrame, text = "Kontrollera", command = check)
kontrollera_knapp.pack(side="left")
info_knapp = Button(topFrame, text = "Info")
info_knapp.pack(side="left")

svarLabel = Label(midFrame, text = "")


spara_knapp = Button(bottomFrame, text = "Spara Palindrome")
spara_knapp.pack(side="left")
avsluta_knapp = Button(bottomFrame, text = "Avsluta")
avsluta_knapp.pack(side="right")

def check():

    x = str(ment.get())
    c = paliCheck.check(x)

    if c == True:
        svarLabel.config(text="Din inmatning är ett Palindrome")

    else:
        svarLabel.config(text="Din inmatning är inte ett Palindrome")


mGui.mainloop()
   
if __name__=="__main__":
    main()
