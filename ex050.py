s = 0
for c in range(1, 7):
    n = int(input("Digite um número inteiro "))
    if n % 2 == 0:
        s += n
    elif n % 2 != 0:
        print("Desconsidere")
else:
    print('A soma dos números pares é {}'.format(s))

