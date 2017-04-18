# Esercizio n. 9
# Trovare i numeri primi in una lista di numeri da 1 fino a 20.

lista = [8, 1, 3, 5, 4, 9, 20, 12, 15, 11, 2, 19, 10, 13]
primi = (2, 3, 5, 7, 11, 13, 17, 19)

for num in lista:
    if num in primi:
        print("Il numero", num, "è primo")
