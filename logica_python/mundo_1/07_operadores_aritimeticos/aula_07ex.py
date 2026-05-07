nome = input ('qual seu nome:')
print('prazer em te conhecer {:>20}!'.format (nome))
n1 = int(input('um valor: '))
n2 = int(input('outro valor: '))
s = n1+n2
m = n1 * n2
d = n1/n2
di = n1 // n2
e = n1 ** n2
print('asoma e {}, \n o produto e {} e a \n divisao e {:.3f}'.format(s, d), end=' ')
print('divisao inteira {} e potrcia {}' .format(di, e, ))
print('a soma vale {}' .format(n1+n2))
