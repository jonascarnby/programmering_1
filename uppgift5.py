# -* coding UTF-8 -*-

"""
Jonas Carnby
Python Ver 3.4.1
OSX 10.9.5
Uppgift 5
"""

#importerar Tkinter och koden från tidigare uppgift 
import sys
from tkinter import *
import tkinter.messagebox
import JonasCarnbyUppgift3py3 as paliCheck

#Funktion för att kontrollera Palindromdet 
def check(to_check=None):

    x = str(ment.get())
    x = x.lower()
    arranged = paliCheck.arrange(x)
    result = paliCheck.showresult(arranged)
    

    if result == True:
        svarLabel.config(text="Din inmatning är ett Palindrome",fg="green",font= ("helvetica", 16))
        spara_knapp.config(state=NORMAL)

    else:
        svarLabel.config(text="Din inmatning är INTE ett Palindrome",fg="red", font=("helvetica", 16))

#Funktion för att spara ett godkänt result 
def save(result):
    if not check(result):
        return
    f = open("Palindromesave", 'a')
    f.write(result+"\n")
    f.close()

    #försök till info om sparning
    svarLabel.config(text="Ditt Palindrome är sparat" ,fg="green")

#Funktion för att avsluta programmet
def quit():

    result = messagebox.askyesno('Avsluta programmet', 'Vill du verkligen avsluta programmet?')
    if result == True:
        mGui.destroy()

#Funktion för att visa information kopplad till info_knapp 
def info():

    messagebox.showinfo("Info","I det här programmet kan du kontrollera om ett visst ord är ett Palindrome.\
 Är ordet ett palindrome har du också möjlighet att spara detta till en separat fil genom att klicka på Spara-knappen ")

    
#Main GUI
mGui = Tk()
mGui.geometry("600x200+300+300")
topFrame = Frame(mGui)
topFrame.pack()
midFrame = Frame(mGui)
midFrame.pack()
bottomFrame = Frame(mGui)
bottomFrame.pack()
bottomFrame.config(width="300")

ment = StringVar()
mGui.title("Palindrome?")

#Knappar och labels i Topframe
topLabel = Label(topFrame, text = "Skriv in texten du vill kontrollera: ")
topLabel.pack(side="left")
uInput = Entry(topFrame, textvariable = ment)
uInput.pack(side="left")
kontrollera_knapp = Button (topFrame, text = "Kontrollera", command = check)
kontrollera_knapp.pack(side="left")
info_knapp = Button(topFrame, text = "Info", command = info)
info_knapp.pack(side="left")

#midFrame
svarLabel = Label(midFrame, text = "")
svarLabel.pack()

#bottomFrame
avsluta_knapp = Button(bottomFrame, text = "Avsluta", command = quit)
avsluta_knapp.pack(side="bottom")
spara_knapp = Button(bottomFrame, text = "Spara Palindrome", command = lambda: save(ment.get()))
spara_knapp.config(state=DISABLED)
spara_knapp.pack(side="bottom")


mGui.mainloop()
   
