import math

a = int(input('Digite o ângulo que você deseja: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))

print('O ângulo {} tem o seno de {:.2f}'.format(a , s))
print('O ângulo {} tem o cosseno de {:.2f}'.format(a , c))
print('O ângulo {} tem a tangente de {:.2f}'.format(a , t))
