from Librairie import *

print("/****/ __ Bienvenue sur vôtre scrapper préférer __ /****/ \n       01 Récuperer des données \n       02 Chercher des données")
choix = int(input("Vôtre choix : "))

if choix == 1:
    recup_data()
elif choix == 2:
    print("Les differents parkings sont : ")
    afficher_parking(parking)
    parking_cherchee = str(input("Saisir un nom de parking sous la forme (Nom) : "))
    DateTime, Free, Total = chercher_donnee(parking_cherchee)
    print("Liste DateTime : ",DateTime)
    print("Liste Free : ",Free)
    print("Liste Total : ",Total)