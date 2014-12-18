# -*- coding: UTF 8 -*-


def createShoppinglist():

    shoppingLst = [];
    print ("avsluta inmatningen genom att lämna fältet tomt")

    while True:

        try:
            item = input("ange en vara du vill köpa:")
            if(item):
                quantity = int(input("ange antal")
                (item) = item.strip().capitalize()
                (shoppingLst).append( str(quantitiy) + "x" + (item)
            else:
                break
                
        except ValueError:
                    print ("du måste mata in ett korrekt värde")

    return (shoppingLst)


def showShoppingList(shoppingList):

    print: ("du har" + str(len(shoppingList)) + "olika produkter att köpa")
        for (item) in (shoppingList):
                print (item)



def main ():

    shoppinglist = createShoppinglist()
    showShoppingList(shoppingList)

main()
