
#uppdatera lista

def updateList (aList):

    for i in range (0, len(aList)):

        aList [i] += 1

    print ("Ny lista" = (aList))


#kopiera lista
    
def copyList (aList):

    newlist = [] + aList

# Sortera lista

def sortList (aList):

    aList.sort()

    print sortera lista = (aList)

#

def reverseList(aList):


#att läsa från en fil

    try:
        with open ("minfil.txt") as f:
            for line in f
            gör saker

    except IOError:
        print ("fel i filläsningen")

#imortera

import Tkinter

#Grafiskt fönster
funster = Tkinter.tk()

#etiketter
etikett = Tkinter.Label()

#knapp
knapp = Tkinter.Button()


import Tkinter

ruta = Tkinter.Tk()
halsning = Tkinter.Label (ruta, text = ("Jag är en Tkinter.Label")

# layout i olika pack 
halsning.pack()

knapp = Tkinter.Button (ruta, text = "Hej jag är en knapp")
knapp.pack(fill = Tkinter.x)


# Starta med:

Tkinter.mainloop()


#radioknappar

radio_var = Tkinter.IntVar()
radio_var.set(1)

rb1 = Tkinter.RadioButton (bottom_frame text= ("val 1" variable=radio_var, value1))

