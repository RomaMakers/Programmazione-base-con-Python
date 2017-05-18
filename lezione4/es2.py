def media(lista):
    lunghezza = len(lista)
    somma = 0

    # indice  = 0
    # while indice < lunghezza:
    #     somma = somma + lista[indice]
    #     indice += 1

    for i in lista:
        somma = somma +  i

    return somma / lunghezza

def stampa(mostra):
    print(mostra)

# main
stampa("Calcolo media")
l = [3,5,2,8,9,3,11,5,1,9,2]
print(" La media dei numeri dati: ", media(l))
