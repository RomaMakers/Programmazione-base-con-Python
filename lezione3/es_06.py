# Esercizio n. 6
# Scrivere un programma “Conto alla rovescia”: inserendo un numero n, finché (while) n è più grande di 0 stampi il
# valore di n e poi lo diminuisca di 1. Quando arriva a 0 stampi la stringa “Partito!".

n = int(input("Introdurre il numero "))
print("Conto alla rovescia:")
while n > 0:
    print(n)
    n = n - 1
    if n == 0:
        print("Partito!")
