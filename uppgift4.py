# -*- coding: UTF-8 -*-

"""
Jonas Carnby
Python Ver.3.4.1
OSX 10.9.5
"""
import celsiusconvert as omvandlare
import sys
from tkinter import *

def convert():

    try:
        
        x = int(ment.get())
        c = omvandlare.convert(x)

        uinput = Label(mGui,text = "Din inmatning är i grader celsius:")
        uinput.pack()
    
        if c <= 0:
            mlabel2 = Label(mGui,text = c, fg="blue" )
            mlabel2.pack()

        else:
            mlabel2 = Label(mGui,text = c, fg="orange" )
            mlabel2.pack()

    except ValueError:
            mlabel3 = Label(mGui,text = "Du måste skriva in ett helt tal, försök igen!", fg = "red")
            mlabel3.pack()

def quit():
    result = messagebox.askyesno('Avsluta programmet', 'Vill du verkligen avsluta programmet?')
    if result == True:
        mGui.destroy()    

omvandlare.convert
   
mGui = Tk()
mGui.geometry("300x200+200+200")
mGui.title("Farenheit Converter")

ment = StringVar()

fLabel = Label(text="Skriv in antal grader i Farenheit:")
fLabel.pack()
fInput = Entry(mGui,textvariable=ment)
fInput.pack()
omvandla = Button(text="omvandla",command = convert)
omvandla.pack()

avsluta = Button(text = "Avsluta",command = quit)
avsluta.pack(side="bottom")




mGui.mainloop()
