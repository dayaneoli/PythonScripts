from datetime import date
nas = int(input('Digite o ano de nascimento do atleta '))
atual = date.today().year
idade = atual - nas
print('O atleta tem {} anos'.format(idade))
if idade <=9:
    print('Atleta da categoria MIRIM')
elif idade <= 14:
    print('Atleta da categoria INFANTIL')
elif idade <= 19:
    print('Atleta da categoria JUNIOR')
elif idade <= 25:
    print("Atleta da categoria SÊNIOR")
else:
    print('Atleta da categoria MASTER')

