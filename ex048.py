s = 0
cont = 0
for c in range(1,501):
    if (c%3 == 0 and c % 2 != 0):
        print(c)
        s += c
        cont += 1
print("A soma dos {} valores é {}".format(cont, s))

