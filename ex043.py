peso = float(input('Digite o seu peso em (kg) '))
altura = float(input('Digite a sua altura em (m) '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Você está ABAIXO DO PESO')
elif imc <= 25:
    print('Você está com o PESO IDEAL')
elif imc <= 30:
    print("Você está com SOBREPESO")
elif imc <= 40:
    print("Você está com OBESIDADE")
else:
    print('Você está com OBSEIDADE MÓRBIDA')
print('imc {:.1F}'.format(imc))



