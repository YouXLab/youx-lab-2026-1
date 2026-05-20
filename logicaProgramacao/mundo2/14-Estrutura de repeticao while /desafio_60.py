from math import factorial
n = int(input('Digite um numero para calcular sua fatorial:'))
c = n
f = 1
print('Calculando {}! = '.format(n), end= '')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end= '')
    c -= 1
 # print('O fatoraial de {} e {}.'.format(n, f))
