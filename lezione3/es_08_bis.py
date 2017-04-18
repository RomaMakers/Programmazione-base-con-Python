# Esercizio n. 8
# Esaminare una lista di numeri e contare il numero di volte in cui ciascuno di questi numeri cade in un
#  determinato intervallo.

num1 = int(input("Introdurre il primo estremo dell'intervallo "))
num2 = int(input("Introdurre il secondo estremo dell'intervallo "))
lista = [3, 5, 7, 11, -2, 4, -7, 5, 0, 13]

if num1 > num2:
    inf = num2
    sup = num1
else:
    inf = num1
    sup = num2

conta = 0
intervallo = range(inf, sup + 1)
for n in lista:
    if n in intervallo:
        conta = conta + 1
print("I numeri nella lista", lista, "\n sono presenti", conta, "volte nell'intervallo [", inf, ":", sup, "]")
