# -*- coding: UTF-8 -*-

"""
Jonas Carnby
Python Ver.3.4.1
OSX 10.9.5
Uppgift 4
"""

#importerar Tkinter samt koden från tidigare uppgift 
import celsiusconvert as omvandlare
import sys
from tkinter import *

#Konverteringsfuktionen samt utskrivning av svaret
def convert():

    try:
        
        x = int(ment.get())
        c = omvandlare.convert(x)

        if c <= 0:
            svarLabel.config(text = "Din inmatning är "+str(c)+" grader i Celsius", fg="blue" )
        
        else:
            svarLabel.config(text= "Din inmatning är "+str(c)+" grader i Celsius", fg="orange")
        
    except ValueError:
            svarLabel.config(text="Du måste skriva in ett heltal, försök igen!", fg="red")

def quit():
    result = messagebox.askyesno('Avsluta programmet', 'Vill du verkligen avsluta programmet?')
    if result == True:
        mGui.destroy()    

omvandlare.convert
   
mGui = Tk()
mGui.geometry("300x200+200+200")
mGui.title("Farenheit Converter")

ment = StringVar()

#Statisk label
fLabel = Label(text="Skriv in antal grader i Farenheit:")
fLabel.pack()

# textfält för att kunna skriva in tempraturen i Farenheit
fInput = Entry(mGui,textvariable=ment)
fInput.pack()

#Knapp för att omvandla 
omvandla = Button(text="omvandla",command = convert)
omvandla.pack()

#Labels som används i convert()
felLabel = Label(text="")
felLabel.pack()
svarLabel = Label(text="")
svarLabel.pack()

#Knapp för att avsluta programmet
avsluta = Button(text = "Avsluta",command = quit)
avsluta.pack(side="bottom")


mGui.mainloop()
