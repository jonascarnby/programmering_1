# -*- coding: UTF-8 -*-

"""
Second go at celcius converter
Python Ver. 3.4.1
Mac OS X 10.9
"""

#Celsius input
def celsius():

    while True:
        
            try:
                tempA = float(input("Skriv in grader i Farenheit: "))

                return tempA
                
            except ValueError:
                print ("Skriv in en siffra, försök igen: ")
            continue
        
#converting from Celsius to Farenheit
def convert(tempF):
     
     tmp = (tempF - 32) * (5/9)
     return round (tmp,2)

#printing answer to user
def svar(tempC):

    print ("Det du skrev i Farenheit är" ,tempC,"grader i celsius")

def main():

    tempF = celsius()
    tempC = convert(tempF)
    svar(tempC) 
    
    
    
main()
