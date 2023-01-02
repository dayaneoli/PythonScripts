somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = " "
totalmulher20 = 0
for p in range(1,5):
    print('-----{}ª PESSOA-----'.format(p))
    nome = str(input("Digite seu nome completo ")).strip()
    idade = int(input("Digite a idade "))
    sexo = str(input('Qual é o sexo M/F ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulher20 += 1
mediaidade = somaidade / 4
print('A média das idades é {:0}'.format(mediaidade))
print('O homem mais velho se chama {} e tem {} anos'.format(nomevelho, maioridadehomem))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totalmulher20))


