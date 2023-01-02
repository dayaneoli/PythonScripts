r1 = float(input('Digite o primeiro segmento de reta '))
r2 = float(input('Digite o segundo segmento de reta '))
r3 = float(input('Digite o terceiro segmento de reta '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3< r1 + r2:
    print('Os segmentos de reta formam um triângulo')
else:
    print('Não é possivel formar um triângulo com estes segmentos de reta')

