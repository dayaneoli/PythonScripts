n1 = float(input('Digite o valor da primeira nota '))
n2 = float(input('Digite o valor da segunda nota '))
media = (n1 + n2) / 2
if media < 5:
    print('Sua média foi {:.2f} e você foi REPROVADO'.format(media))
elif media > 5 and media <=6.9:
    print('Sua média foi {:.2f} e você está de RECUPERAÇÃO'.format(media))
elif media > 7:
    print('Sua média foi {:.2f} e você foi APROVADO!'.format(media))




