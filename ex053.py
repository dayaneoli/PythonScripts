frase = str(input("Digite uma frase para saber se é palíndromo ou não ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
        print('A frase é um Palíndromo')
else:
        print("A frase não é um Palíndromo")



