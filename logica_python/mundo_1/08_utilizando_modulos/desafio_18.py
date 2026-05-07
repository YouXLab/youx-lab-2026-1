from math import radians, sin, cos, tan
angulo  = float(input('digite o ãngulo que voce deseja: '))
seno = sin (radians(angulo))
print('o seno de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = cos (radians(angulo))
print('o angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
