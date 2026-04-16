import math
N1 = float(input('Comprimento do cateto oposto: '))
N2 = float(input('Comprimento do cateto adiante: '))
N3 = math.hypot(N1,N2)

print('{:.2f}'.format(N3))