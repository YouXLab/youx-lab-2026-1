import math

ca = float(input('Digite o comprimento do cateto adjacente: '))
co = float(input('Digite o comprimento do cateto oposto: '))
h = (ca ** 2 + co ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(h))
print('A hipotenusa vai medir {:.2f}'.format(math.hypot(co, ca)))
