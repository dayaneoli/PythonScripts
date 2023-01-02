produto = float((input('Insira o valor do produto R$ ')))
vista = produto - ((produto*5/100))
prazo = produto + ((produto*5/100))
print('O produto a vista custa R$ {:.2f}. O produto a prazo custa R$ {:.2f}'.format(vista, prazo))
