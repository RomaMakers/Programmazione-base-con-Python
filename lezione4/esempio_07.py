def trasla(x, y, z, n=2):
    a = x + n
    b = y + n
    c = z + n
    return a, b, c


x1, y1, z1 = trasla(z=3, x=6, y=9)
print(x1, y1, z1)
