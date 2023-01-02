sexo = str(input("Digite seu sexo [M/F] ")).strip().upper()[0]
'''Elimina espaços, deixa tudo em letras maiúsculas e pega somente a primeira letra'''
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, digite novamente [M/F] ')).strip().upper()[0]
print('Sexo {} digitado com sucesso'.format(sexo))

