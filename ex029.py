vel = float((input('Digite a velocidade do veículo em km/h ')))
if vel > 80:
    print("Você foi multado")
    multa = (7 * (vel - 80))
    print("A multa é de R$ {:.2f}".format(multa))
else:
    print('Você não foi multado!')
print('Dirija com segurança!')
