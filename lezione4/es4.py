def stampa(num, testo):
    '''Stampa un testo num volte'''
    for i in range(num):
        print(testo)


#main
scri = input(" cosa vuoi scrivere? ")
num = int(input(" Quante volte? "))
stampa(num,scri)
