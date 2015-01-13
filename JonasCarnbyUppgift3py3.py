# -*- coding: UTF-8 -*-


"""
Jonas Carnby
Python ver 3.4.1
OSX 10.9.5
"""


def main():

    while True:

    
        pali = createlist() 
        
        
        arrangedpali = arrange(pali)
        

        palindrome = showresult(arrangedpali)
        if palindrome == True:
            print ("Det här är ett Palindrome!")

        else:
            print ("Det här är INTE ett Palindrome")
        

            
# take input and create a list
def createlist():

    ret = []

    while True:
        
        try:
            word = list(input("Skriv det ordet du vill du vill kontrollera: ").lower())

            ret.extend(word)

        except ValueError:
            print ("Skriv in ett ord")

        break

    return (ret)

# arrrange list and remove unwanted symbols       
def arrange(arrange_word):

    ret = []
    symbols = ("'${} ()[].,:;+-*/&!|<>=~")
    
    
    for bokstäver in arrange_word:
        
        if bokstäver not in symbols:
            ret.append(bokstäver)    

        
    return (ret)
    
    
# reverse list and check if it is a palindrome
def showresult(check_palindrome):

    
    palindrome = []

    for c in range(len(check_palindrome)):
        
        if check_palindrome[c] != check_palindrome [-c-1]:
            return False
            
    return True
                


if __name__=="__main__":
    main()
