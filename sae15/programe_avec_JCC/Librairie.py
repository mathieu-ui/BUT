## Importaa
##########

from pydoc import text
from unittest import result
import requests
import os
from math import *
import numpy as np
import matplotlib.pyplot as plt
import xml.etree.ElementTree as P
import time
import datetime
import csv

## Valeurs
##########

T=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
L1=[3,3,4,3,2,5,8,9,13,16,18,18,19,21,22,22,21,17,17,12,10,8,7,4]
L2=[103,203,4,3,2,5,8,9,13,16,18,18,19,21,22,22,21,17,17,12,10,-92,-93,-96]
parking = ["FR_MTP_ANTI","FR_MTP_COME","FR_MTP_CORU","FR_MTP_EURO","FR_MTP_FOCH","FR_MTP_GAMB",
"FR_MTP_GARE","FR_MTP_TRIA","FR_MTP_ARCT","FR_MTP_PITO","FR_MTP_CIRC","FR_MTP_SABI","FR_MTP_GARC",
"FR_MTP_SABL","FR_MTP_MOSS","FR_STJ_SJLC","FR_MTP_MEDC","FR_MTP_OCCI","FR_CAS_VICA","FR_MTP_GA109",
"FR_MTP_GA250","FR_CAS_CDGA","FR_MTP_ARCE","FR_MTP_POLY"]

## Moyenne liste
##########
def moyenne_liste(liste):
    '''
    Fonction qui calcule la moyenne d'une liste
    Entrée : Liste
    Sortie : Moyenne de la liste
    '''
    somme = 0

    for i in range (len(liste)):
        somme += liste[i]
    somme = somme / len(liste)
    return somme

## Ecart type liste de nombre
##########
def ecart_type(liste):
    '''
    Fonction qui calcule l'écart type d'une liste
    Entrée : Liste
    Sortie : Moyenne de la liste
    '''
    moyenne = moyenne_liste(liste)
    somme_moyenne = 0
    ecart_type = 0

    for i in range(len(liste)):
        somme_moyenne = ( liste[i] - moyenne )**2
        ecart_type += somme_moyenne
    ecart_type = sqrt(ecart_type / len(liste))
    return ecart_type

## Représentation graphique
##########
def graphique(liste_x,liste_y):
    '''
    Fonction qui fait une représentation graphique
    entrées : liste des x et y
    sortie : graphique en fonction des valeurs de x et y
    Commandes : print("la moyenne de la liste est ",moyenne_liste(L2))
    print("l'écart type de la liste est ",ecart_type(L2))
    graphique(T,L1)
    '''
    x = np.array(liste_x) # Données en X
    y = np.array(liste_y) # Données en Y

    plt.plot(x, y) # Trace la courbe
    plt.title("Evolution température")
    plt.xlabel('Temps')
    plt.ylabel('Température')
    plt.savefig('courbe plt')
    plt.show()

## Supprimer fichier
##########
def supr(parking):
    """
    Fonction qui permet de supprimer tous les fichier .xml lié a la liste des nome de parking
    Entrée : Liste des parkings
    Sortie : Affiche code erreur si il y en a une
    """
    for i in range(len(parking)):
        file = parking[i]+".xml"
        try:
            os.remove(file)
        except OSError as error:
            print(error)
        else:
            print("Fichier supprimé")

## Afficher parking
##########
def afficher_parking(parking):
    for i in range(len(parking)):
        print(parking[i])

## Recupérer_Fxml
###########
def recuperer_Fxml(parking):
    '''
    Fonction qui telecharge le fichier xml de chaque parking
    Entrée : liste des noms de parking
    Sortie : fichier xml de chaque parking
    Commande : recuperer_Fxml(parking)
    '''

    for i in range(len(parking)):
        URL = "https://data.montpellier3m.fr/sites/default/files/ressources/"+parking[i]+".xml"
        response = requests.get(URL)
        print(URL,(response.status_code))

        if response.status_code == requests.codes.ok:
            with open(parking[i]+".xml", 'wb') as fichier:
                fichier.write(response.content)
        else:
            while response.status_code != True:
                URL = "https://data.montpellier3m.fr/sites/default/files/ressources/"+parking[i]+".xml"
                with open(parking[i]+".xml", 'wb') as fichier:
                    fichier.write(response.content)


## Parser les xml
##########
def parser_xml(parking):
    '''
    Fonction qui permet de recuperer des éléments dans un fichier xml
    Entrée : Nom du parking sous la forme "FR_MTP_ANTI"
    Sortie : Liste contenant les données selectionné
    commande : parser_xml("FR_MTP_ANTI")
    [0] = DateTime, [1] = Name, [2] = Status, [3] = Free, [4] = Total
    '''
    resultat = []
    for x in range(len(parking)):
        r = []
        fichier = parking[x]+".xml"
        print(fichier)
        tree = P.parse(fichier)
        root = tree.getroot()

        r.append(parking[x]), r.append(root[0].text), r.append(root[3].text), r.append(root[4].text) # créer une liste : [Name,DateTime,free,total]
        resultat.append(r)
    return resultat

## Ecrire fichier
##########
def ecrire_fichier():
    '''
    Programme qui permet d'écrire les données du parking dans un csv
    Entrée : ...
    Sortie : ...
    Commande : ...
    '''
    resultat = parser_xml(parking)
    with open("data_voiture.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(resultat)
    f.close()
    

## Boucle recupération data
##########
def recup_data():
    nb = int(input("Combien de serie de données voulez vous recupérer : "))
    tps = int(input("Combiend de secondes de pause entre chaque serie de données : "))
    tps_t = (tps + 15)*nb
    print("Vous avez choisie de recupérer ",nb,"données, avec ",tps," secondes de pause entre chaque serie. Le temps nessésaire est d'environ ",datetime.timedelta(seconds=tps_t))

    for i in range(nb):
        print("Nombre de serie de données recuperer : ", i)
        time.sleep(tps)
        recuperer_Fxml(parking)
        ecrire_fichier()
        time.sleep(1)
        supr(parking)

## chercher les données
##########
def chercher_donnee(parking_cherchee):
    """
    Fonction qui permet de recupérer les données d'un parking [Name,DateTime,free,total]
    Entrée : ...
    Sortie : ...
    Commande : ...
    """
    DateTime = []
    Free = []
    Total = []

    reader = csv.reader(open("data_voiture.csv","r"))
    for row in reader:
        if row[0] == parking_cherchee:
            DateTime.append(str(row[1]))
            Free.append(int(row[2]))
            Total.append(int(row[3]))

    return DateTime, Free, Total