def area_quadrato(lato):
    area = lato * lato
    return area

def area_rettangolo(lato1, lato2):
    area = lato1 * lato2
    return area

def area_cerchio(raggio):
    return raggio * raggio * 3.14

#Programma Principale
l = int(input(" inserisci la misura del lato del quadrato "))
area = area_quadrato(l)
print(" L'area del quadrato: ", area)

lato1 = 5
lato2 = 9
l1 = int(input(" inserisci la misura del primo lato del rettangolo "))
l2 = int(input(" inserisci la misura del secondo lato del rettangolo "))
area = area_rettangolo(lato2=l1, lato1=l2)
print(" L'area del rettangolo: ", area)