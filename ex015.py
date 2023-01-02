km = float((input('Quantos quilômetros foram rodados?')))
d = int((input('Por quantos dias o carro foi alugado')))
td = 60.00 * d
kmr = 0.15 * km
tl = td + kmr
print('O valor total a pagar é R$ {:.2f}'.format(tl))





