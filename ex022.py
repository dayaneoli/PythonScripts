nome = str((input("Digite seu nome"))).strip()
lm = nome.upper()
lmn = nome.lower()
separa = nome.split()
print("nome com letras maiúsculas {} e letras minúsculas {}".format(lm, lmn))
print("Quantidade total de letras sem contar espaços é {}".format(len(nome) - nome.count(' ')))
print('O primeiro nome é {} e tem {} letras'.format(separa[0],len(separa[0])))













