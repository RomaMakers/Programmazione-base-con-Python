# Esercizio n. 3
# Scrivere un programma che dati due numeri, li visualizza in ordine crescente (o decrescente).

num1 = int(input("Introdurre il primo numero "))
num2 = int(input("Introdurre il secondo numero "))
print("I numeri in ordine decrescente:")
if num1 > num2:
    print(num1, "\t", num2)
else:
    print(num2, "\t ", num1)
