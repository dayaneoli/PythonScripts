numero = int(input("Digite um número inteiro "))
tot = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print("{}".format(c), end=' ')
print('\n\033[m O número {} foi divisível {} vezes'.format(numero, tot))
if tot == 2:
    print('E por isso ELE É PRIMO')
else:
    print('E por isso ELE NÃO É PRIMO')


''' Números Primos (Se o número for divisível fica amarelo, se não for, fica vermelho)'''