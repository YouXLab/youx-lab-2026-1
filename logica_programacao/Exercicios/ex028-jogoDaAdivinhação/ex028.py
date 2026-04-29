from random import randint
computador = randint(0, 5)
print('Irei pensar em um numero entre 0 e 5.Tente adivinhar.')
jogador = int(input('Em que numero eu pensei?'))
if jogador == computador:
    print('PARABÉNS! voce conseguiu me vencer!')
else:
    print('GANHEI! eu pensei no numero {}  e não no {}!'.format(computador, jogador))