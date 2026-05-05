Numero = int(input('Informe um numero: '))
U = Numero // 1 % 10
D = Numero // 10 % 10
C = Numero // 100 % 10
M = Numero // 1000 % 10
print('Seu numero tem:')
print('Unidade: {}'.format(U))
print('Dezena: {}'.format(D))
print('Centena: {}'.format(C))
print('Milhar: {}'.format(M))
