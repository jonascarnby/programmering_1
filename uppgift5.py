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

mGui = Tk()
mGui.geometry("600x300+300+300")
topFrame = Frame(mGui)
topFrame.pack()
midFrame = Frame(mGui)
bottomFrame = Frame(mGui)


mGui.title("Palindrome?")

topLabel = Label(text = "Skriv in texten du vill kontrollera nedan")
topLabel.pack(topFrame)



mGui.mainloop()
