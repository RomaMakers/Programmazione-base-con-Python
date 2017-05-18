def confronta(x,y):
    if x < y:
        num1 = x
        num2 = y
    else:
        num1 = y
        num2 = x
    return num1, num2

def confronta2(x,y):
    if x < y:
        return x,y
    else:
        return y,x

#main
a,b = 7,5
o1,o2 = confronta(a,b)
print(o1,o2)
print(confronta2(3,5))

