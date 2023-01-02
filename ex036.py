casa = float(input('Valor da casa R$ '))
salario = float(input('Salário do comprador R$ '))
anos = int(input('Quantos anos de financiamento '))
prestacao = casa / (anos * 12)
simu = prestacao / salario
if simu == 0.30 or simu < 0.30:
    print('Seu empréstimo foi aprovado')
else:
    print('Seu empréstimo foi reprovado')
print('O valor do financiamento é {:.2f}, divididos em {} anos, com parcelas de R$ {:.2f}'.format(casa, anos, prestacao))

