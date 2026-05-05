import math
N1 = float(input('Qual a velocidade do seu carro? '))
N2 = (N1 - 80) * 7
N3 = 80 * 1.07
if N1 >= N3:
    print('Você foi multado em R${:.2f}'.format(N2))
else:
    print('Você não foi multado')
