# -*- coding: UTF-8 -*-

"""
Jonas Carnby
Python ver. 3.4.1
Mac OS X 10.9
"""

# 27st förinskrivna tempraturer 
templist = [2, 3, 4, 2, 5, 2, 1, 0, -1, -3, -10, -5, -1, -3, -5, -7, -7, -10, -12, -7, -5, -6, -10, -5, -5, -4, -3]

def main():

     while True:
          
          choosefunction()          

# Skriver ut den lägsta tempraturen från "templist"    
def lowTemp():
    
    print ("\n Den lägsta tempraturen i December var:",(min(templist)))

# Skriver ut den högsta tempraturen från "templist"
def highTemp():

    print ("\n Den högsta tempraturen i December var:",(max(templist)))

# Skriver ut medeltempraturen från "templist"
def avgTemp():

    tmp = (sum(templist)/len(templist))
    print ("\n Medeltempraturen för december är:",(round(tmp, 2)))

# Skriver ut hela månadens tempraturer
def monthTemp():
    
    print ("Dagarna i december har haft följande tempraturer:")
    for temp in templist:
        print ("\t",temp)

# Addera grader till listan
def adddegree():


     if len(templist) >= 31:
          print ("December har bara 31 dagar och listan är full")
          return
     
     else:

          try:
              add = int(input("skriv dagens tempratur i helttal: "))

              templist.append(add)
                    
          except ValueError:
               print ("Skriv in ett heltal! Försök igen.")

# Här väljer användaren vilken information hen vill granska 
def choosefunction():

    while True:

        try:
            function = input("\n Ange vilken information du vill granska. Du kan välja mellan: \n \t Lägg till dagens grad (T) \n \t Högsta(H)\n \t Lägsta(L)\n \t \
Medeltempratur(M) \n \t Tempraturen för alla dagar(A) \n \t Avsluta genom att skriva (X) \n \t \n \t Välj: ")

            if  ("h") == function or ("H") == function:
                return highTemp()

            elif ("L") == function or ("l") == function:
                return lowTemp()

            elif ("M") == function or ("m") == function:
                return avgTemp()

            elif ("A") == function or ("a") == function:
                return monthTemp()

            elif ("T") == function or ("t") == function:
                 return adddegree()
     
            elif ("X") == function or ("x") == function:
                exit()

            else:
                print ("\n Skriv in någon av de nämnda bokstäverna, försök igen")
                

        except ValueError:
            ("Skriv in en av de nämnda bokstäverna")

main()
