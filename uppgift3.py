# -*- coding: UTF-8 -*-



def main():

    while True:

        pali = createlist() 
        print (pali)
        
        # next thing with pali (arrange)
        
        arrangedpali = arrange(pali)
        

        # reverse word and see if it is a palindrome

        palindrome = showresult(arrangedpali)
        print (palindrome)

def createlist():

    ret = []

    while True:
        
        try:
            word = list(input("Skriv det ordet du vill du vill kontrollera: "))

            ret.extend(word)

        except ValueError:
            print ("Skriv in ett ord")

        break

    return (ret)

        
def arrange(arrange_word):

    ret = []
    symbols = ("'${} ()[].,:;+-*/&!|<>=~")
    
    
    for bokstäver in arrange_word:
        
        if bokstäver not in symbols:
            ret.append(bokstäver)    

        
    return (ret)
    
    

def showresult(check_palindrome):

    
    palindrome = []
    
    for c in check_palindrome[::-1]:
        palindrome.append(c)


        word = "".join(palindrome)
        print (word)
         

        

        
    
        return (palindrome)


main()
