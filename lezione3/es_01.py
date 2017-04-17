# Esercizio n. 1
# Scrivere il programma per controllare se un numero è positivo.

num = int(input("Introdurre il numero "))

if num > 0:
    print(num, "è positivo")
elif num == 0:
    print("Il numero è zero")
else:
    print(num, "è negativo")
