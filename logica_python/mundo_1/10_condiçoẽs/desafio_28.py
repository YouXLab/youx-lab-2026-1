from random import randint
from time import sleep
computador = randint(0, 5)# faz o computador "PENSAR"
print('_=_' * 20)
print('vou pensar em um número entre 0 e 5. tente adivinhar...')
print('_=_' * 20)
jogador = int(input('em que número eu pensei? ')) # jogador tenta adivinhar
sleep(3)
if jogador == computador:
    print('PARABÉNS! vocẽ conseguiu me vencer!')




