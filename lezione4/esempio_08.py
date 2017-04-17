def fib(n):
    """Restituisce la serie di Fibonacci fino a n"""

    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


print(fib(90))
