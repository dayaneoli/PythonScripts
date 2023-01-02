r = int(input("Digite a razão da progressão aritmética "))
a1 = int(input("Digite o primeiro termo da progressão aritmética "))
décimo = a1 + (10 - 1) * r
for c in range(a1, décimo + r, r):
    print("{} ".format(c), end=' ')
print('ACABOU O PROGRAMA!')

'''PROGRESSÃO ARITMÉTICA'''
