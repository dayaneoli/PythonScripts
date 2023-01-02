salario = float(input('Digite o valor do seu salário R$ '))
if salario > 1250:
    aum = (salario * 0.10) + salario
else:
    aum = (salario * 0.15) + salario
print('Você passará a receber R$ {:.2f}'.format(aum))
