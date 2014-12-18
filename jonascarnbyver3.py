"""
Jonas Carnby
Python version 3.4.1
OS X 10.9.5
"""

def inmatning():
    while True:  
        try:
            tempA = float (input ("Hej, skriv in tempraturen i grader Farenheit:"))

            return tempA
   
        except ValueError:
            print ("Skriv in en siffra utan decimaler: ")
        continue

def uträkning(tempB):
    
    tmp = (tempB - 32) * (5/9)
    return round(tmp,2)
    
def svar(tempD):

    print ("Din inmatning är:",tempD,"grader i celcius") 

def main():

    tempF = inmatning()
    tempC = uträkning(tempF)
    svar(tempC)

main()
