from uuid import NAMESPACE_X500

N1 = float(input('Escreva um numero: '))

N2= N1 * 0.001
N3= N1 * 0.01
N4= N1 * 0.1
N5= N1 * 10
N6= N1 * 100

print('{:.3f}km'.format(N2))
print('{:.2f}hm'.format(N3))
print('{:.1f}dam'.format(N4))
print('{}m'.format(N1))
print('{}cm'.format(N5))
print('{}mm'.format(N6))