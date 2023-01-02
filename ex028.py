import random
from time import sleep
print('-=-' * 10)
print('Tente ganhar do computador')
print('-=-' * 10)
esc = int((input('Tente adivinhar qual número entre 0 e 5 o computador escolheu '))) #jogo de adivinhar qual nº o computador escolheu
num = random.randint(0,5)
print('PROCESSANDO...')
sleep(3)
if esc == num:
    print('Você ganhou! Eu pensei no número {}'.format(num))
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(num, esc))



