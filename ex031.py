print('-' * 45)
print('Programa que calcula o valor da sua viagem?')
print('-' * 45)
dist = float(input('Qual a distância da sua viagem em km? '))
if dist <= 200:
    vvp = 0.50 * dist
    print('O valor total da sua passagem é R${:.2f}'.format(vvp))
else:
    vvl = 0.45 * dist
    print('O valor total da sua passagem é R${:.2f}'.format(vvl))
print('Obrigado por usar esse programa!')

