from os import read
import os
import requests
from lxml import etree 
import time

file1 = 'data_parkings.log'
file2 = 'parkings.log'

os.remove(file1)
os.remove(file2)

parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT',
'FR_MTP_PITO','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_GARC','FR_MTP_SABL','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY'] 
# ici la liste des parkings

f1=open("parkings.log","a", encoding='utf8')
f2=open("data_parkings.log","a", encoding='utf8')

liste_des_parking = []
# ici creation de la liste dans laquel on vas stoquer les données 


temps_donne = 30
temps_iteration = 5

nombre_iteration =round (temps_donne / temps_iteration)


for y in range(nombre_iteration):
    for i in range(len(parkings)):
        liste_provisoir = []

        url="https://data.montpellier3m.fr/sites/default/files/ressources/"+parkings[i]+".xml"
        print(url)
        response=requests.get(url)

        tree = etree.fromstring(response.content)

        for user in tree.xpath("Name"):
            print('Nom du parking :',user.text)
            f1.write(f"Nom du parking : {user.text}\n")
            liste_provisoir.append(user.text)
            f2.write(f"{user.text}\n")

        for user in tree.xpath("Total"):
            place = user.text
            print('Nombre total de places :',user.text)
            f1.write(f"Nombre total de places : {user.text}\n")
            liste_provisoir.append(user.text)
            f2.write(f"{user.text}\n")

        for user in tree.xpath("Free"):
            place_libre = user.text
            print('Nombre de places libres :',user.text)
            f1.write(f"Nombre de places libres : {user.text}\n")
            liste_provisoir.append(user.text)
            f2.write(f"{user.text}\n")

        liste_des_parking.append(liste_provisoir)

        place_libre = int(place_libre)
        place = int(place)
        pour_cent = str(round((place_libre * 100)/place))

        print("Pourcentage de place libre : "+pour_cent+" %")
        f1.write(f"Pourcentage de place libre : "+pour_cent+" %\n")
    time.sleep(temps_iteration)

f1.close() 
f2.close()

print(liste_des_parking)

f3=open("data_parkings.log","r", encoding='utf8')
data_parking2=[]
for i in range(len(parkings)):
    for h in range(nombre_iteration):
        data_parking1=[]
        for j in range(0,3):
            data_parking1.append(f3.readline().strip('\n'))
        data_parking2.append(data_parking1)
print(data_parking2)
f3.close()

