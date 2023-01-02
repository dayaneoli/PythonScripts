a = int((input("Digite o primeiro valor ")))
b = int((input('Digite o segundo valor diferente do primeiro ')))
c = int((input('Digite o terceiro valor diferente dos outros dois primeiros ')))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))


