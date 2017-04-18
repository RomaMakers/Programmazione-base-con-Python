# Esercizio n. 10
# Trovare i divisori di un numero fornito in input.

num = int(input("Introdurre il numero "))

primo = True

if num < 2:
    print("Un numero inferiore a 2 non può essere primo")
    primo = False
if num == 2:
    primo = True
else:
    if num % 2 == 0:
        print("Il numero", num, "è divisibile per 2")
        primo = False
    for i in range(3, num // 2, 2):
        if num % i == 0:
            print("Il numero", num, "è divisibile per", i)
            primo = False
if primo:
    print("Il numero", num, "è primo")
