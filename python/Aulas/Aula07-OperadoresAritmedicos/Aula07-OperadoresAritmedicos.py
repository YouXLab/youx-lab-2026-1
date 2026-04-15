n= input('Qual seu nome?')
print('prazer em te conhecer {:^20}!'.format(n))

n1= int(input('digite um numero: '))
n2= int(input('digite outro numero: '))
sm= n1 + n2
sb= n1 - n2
m= n1 * n2
d= n1 / n2
di= n1 // n2
e = n1 ** n2
print(' a soma é {},\n a subtração é {},\n a multiplicação é {},\n a divisão é {},\n a divisão inteira é {},\n a potência é {}'.format(sm, sb, m, d, di, e))
