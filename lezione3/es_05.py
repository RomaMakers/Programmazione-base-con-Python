# Esercizio n. 5
# Visualizzare tutti i numeri dispari compresi fra 1 e 50.


n_min = 1
n_max = 50
print("I numeri dispari compresi tra", n_min, "e", n_max, "sono:")
n = n_min
while n <= n_max:
    if n % 2 != 0:
        print(n, "\t")
    n = n + 1
