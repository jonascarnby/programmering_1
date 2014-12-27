# -*- coding: UTF-8 -*-



def main():

    while True:

        pali = createlist() 
        print (pali)
        
        # next thing with pali (arrange)
        
        arrangedpali = arrange(pali)
        print (arrangedpali)

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
    temp = ""
    
    for bokstäver in arrange_word:
        
        if bokstäver not in symbols:
                    temp += bokstäver

    ret.append(temp)

        
    return (ret)
    
    

def showresult(check_palindrome):

    ret = reversed(check_palindrome)

    return (ret)


main()
