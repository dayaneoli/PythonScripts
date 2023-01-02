import math
a = float((input('Digite o valor do ângulo')))
ar = a / 57.2958 #radianos para graus
sen = math.sin(ar)
cos = math.cos(ar)
tan = math.tan(ar)
print('O valor do seno é {:.3f}, do cosseno é {:.3f} e da tangente é {:.3f}'.format(sen, cos, tan))

#ou
from math import radians, sin, cos, tan, trunc
a = float((input("Digite o valor do ângulo")))
seno = sin(radians(a))
print("O valor do seno do ângulo de {} é {:.2f}".format(trunc(a), seno))
cosseno = cos((radians(a)))
print('O valor do cosseno do ângulo de {} é {:.2f}'.format(trunc(a), cosseno))
tangente = tan((radians(a)))
print('O valor da tangente do ângulo de {} é {:.2f}'.format(trunc(a), tangente))








