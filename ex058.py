from random import randint
computador = randint(0, 10)
print('Sou seu computador e, acabei de pensar em um número entre 0 e 10. ')
print('Será que você consegue adivinhar? ')
acertou = False
palpites = 0
while not acertou:
    numjogador = int(input("Tente adivinhar o número "))
    palpites += 1
    if computador == numjogador:
     acertou = True
    else:
        if numjogador > computador:
            print('Menos... Tente novamente! ')
        elif numjogador < computador:
            print("Mais... Tente novamente! ")
print("Você acertou com {} tentativas!".format(palpites))