import random

N1 = random.randint(1, 5)
N2 = int(input('Escreva um numero de 1 a 5: '))
if N2 == 5:
    print('acertou')
else:
    print('errou o numero era {}'.format(N1))
