from random import randint
from time import sleep
coisa = ('pedra', 'papel', 'tesoura')
computador =randint(0, 2)
print('''suas opções:
[0] pedra
[1] papel
[2] tesoura''')
jogador =int(input('qual é sua jogada? '))
print('JÔ')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
print('-='*11)
print('computador jogou {}'.format(coisa[computador]))
print('o jogador jogou {}'.format(coisa[jogador]))
print('-='*11)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR  VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')