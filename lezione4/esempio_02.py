for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'è uguale a', x, '*', n // x)
            break
    else:
        print(n, 'è un numero primo')
