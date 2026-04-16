print('oi' + 'ola')
print('oi' * 5)
print('=' * 20)

nome = input('qual é o seu nome?')
print('prazer em te conhecer {}!'.format(nome))

n1 = int(input('um valor:'))
n2 = int(input('outro valor:'))
print('a soma vale {}'.format(n1 + n2))

n1 = int(input('um valor:'))
n2 = int(input('outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('a soma é {}, o produto é {} e a divisao é {}'.format(s, m, d), end=' ')
print('divisao inteira é {} e potencia {}'.format(di, e))