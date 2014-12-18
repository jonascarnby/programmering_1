# -*- coding: UTF-8 -*-

from random import randint

def main():

    correct = 0
    stop = 5

    for i in range (0, stop,1):
        num1 = randint(0,100)
        num2 = randint(0,100)
        correct += print Q (num1, num2)


def printQ(num1, num2):

    corrAns = num1+num2
    while true:

        try:
            userAnswer = int(input(str(num1)+"+"+ str(num2)+" "))
            if(corrAns==userAnswer):
                print ("korrekt")
                return 1

            else:
                print ("fel")
                return 0
            break
        except ValueError:
            print ("Måste ange ett heltal!")
                       
            
            
