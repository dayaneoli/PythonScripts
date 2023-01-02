from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pess in range(1,8):
    ano = int(input("Digite o {} ano de nascimento ".format(pess)))
    idade = atual - ano
    if atual - ano >= 18:
            maior += 1
    else:
            menor += 1
print('{} são maiores de idade e {} são menores'.format(maior, menor))
