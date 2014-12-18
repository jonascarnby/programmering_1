# -*- coding: UTF-8 -*-



def main():

    while True:

        pali = createlist() 
        print (pali)
        
        # next thing with pali (arrange)
        
        arrangedpali = arrange(pali)
        print (arrangedpali)

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
    symbols = ("'${}()[].,:;+-*/&|<>=~")
    temp = ""
    for element in arrange_word:
    
        for ch in element:
                if ch not in symbols:
                    temp += ch



    ret.append(temp)
    



    pass
    for i in range ( 0, len(arrange_word)):

        if arrange_word[i] != (symbols):
            ret.append(arrange_word)

            print (ret)
            

            

        

    return (ret)
    
    

def showresult():
    pass


main()
