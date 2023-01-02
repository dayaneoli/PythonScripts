from datetime import date
atual = date.today().year
nas = int(input('Digite o ano do seu nascimento '))
idade = atual - nas
print('''Escolha a opção:
[1] feminino
[2] masculino''')
opção = int(input('Sua opção é '))
if opção == 1:
    print('Você não precisa se alistar!')
elif opção == 2 and idade == 18 and idade > 18 and idade < 18:
    idade = atual - nas
    print("Quem nasceu em {}, tem {} anos no ano atual".format(nas, idade))
elif idade == 18:
    print("Você tem que se alistar imediatamente!")
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
elif idade < 18:
    saldo = 18 - idade
    print('Faltam {} anos para você se alistar'.format(saldo))
    ano = 18 - saldo
    ano2 = atual + saldo
    print('Seu alistamento será daqui a {} anos, no ano de {}'.format(saldo, ano2))
print('Obrigado!')

