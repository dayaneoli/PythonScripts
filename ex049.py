n = int(input("Digite um valor para saber sua tabuada "))
for c in range(1, 11):
    tab = n * c
    print('{} x {:2} = {}'.format(n, c, tab))

