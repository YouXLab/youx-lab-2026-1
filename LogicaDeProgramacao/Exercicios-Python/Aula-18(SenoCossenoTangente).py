import math

N1 = float(input('Digite um ângulo: '))

Seno = math.sin(math.radians(N1))
print('O ângulo de {} tem o Seno de {:.2f}'.format(N1,Seno))

Cosseno = math.cos(math.radians(N1))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(N1,Cosseno))

Tangente = math.tan(math.radians(N1))
print('O ângulo de {} tem o Tangente de {:.2f}'.format(N1,Tangente))