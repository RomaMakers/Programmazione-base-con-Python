# Esercizio n. 9
# Trovare i numeri primi in una lista di numeri da 1 fino a 20.

lista = [8, 1, 3, 5, 4, 9, 20, 12, 15, 11, 2, 19, 10, 13]

for num in lista:
    primo = True
    i = 2
    while i < num:
        if num % i == 0:
            primo = False
        i = i + 1
    if primo:
        print("Il numero", num, "è primo")
