from math import sqrt 

def moyenne (liste):
    return sum(liste)/len(liste)

def ecart_type(liste):
    a = moyenne(liste)
    b=[]
    for i in range(len(liste)) :
        b.append((liste[i]-a)**2)
    c = sum(b)
    c = c / len(liste)
    c = sqrt(c)
    return c
