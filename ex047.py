for n in range(1, 51):
    if n % 2 == 0:
        print(n, end=" ")
print('ACABOU!')

# outra forma de fazer e, com menos uso do processador
for c in range(2, 51, 2):
    print(c, end=" ")
print("ACABOU!")