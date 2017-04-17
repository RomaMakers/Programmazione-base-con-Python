# Esercizio n. 2
# Scrivere il programma che controlla il risultato di una addizione, dati due numeri e la loro somma in input.

num1 = int(input("Introdurre il primo addendo "))
num2 = int(input("Introdurre il secondo addendo "))
num3 = int(input("Introdurre la somma "))
somma = num1 + num2
if somma == num3:
    print("La somma è corretta! ")
else:
    print("Il valore è sbagliato!\n La somma è uguale a ", somma)
