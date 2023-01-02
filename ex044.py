print('{:=^100}'.format(' FD DESENHISTA, PROJETISTA E CADISTA '))
preço = float(input('Digite o valor do projeto: R$ '))
print('''Formas de pagamento:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Digite a forma de pagamento escolhida '))
if opção == 1:
    total = preço - (preço * 0.10)
    print('O valor do projeto a vista em dinheiro/cartão é R$ {:.2f}'.format(total))
elif opção == 2:
    total = preço - (preço * 0.05)
    print('O valor do projeto à vista no cartão é de R$ {:.2f}'.format(total))
elif opção == 3:
    total = preço / 2
    print('O valor do total do projeto é R$ {:.2f} e, parcelado em 2x no cartão é R$ {:.2f} cada parcela SEM JUROS'.format(preço, total))
elif opção == 4:
    parcelas = int(input('Digite a quantidade de parcelas 3x ou mais '))
    total = preço + (preço * 0.20)
    parc = total / parcelas
    print('O valor do projeto parcelado em {} parcelas é R$ {:.2f}. Sendo R$ {:.2f} cada parcela COM JUROS'.format(parcelas, total, parc))
else:
    total = 0
    print('Opção inválida. Tente novamente!')
print('{:=^100}'.format(' A FD AGRADECE A SUA PREFERÊNCIA!! '))




