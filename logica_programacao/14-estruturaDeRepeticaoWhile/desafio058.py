#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
# em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

import random
from random import randint
from time import sleep
print('EU...SOU...SEU...COMPUTADOOOOOOOOOOOR!!!')
print('ACABEI DE PENSAR EM UM NÚMERO ENTRE 0 E 10...')
print('SERÁ QUE VOCÊ É CAPAZ DE ADIVINHAR? VAMOS DESCOBRIR...')
computador = randint(0,10)
acerto = False
tentativas = 0
while not acerto:
    palpite = int(input('QUAL O SEU PALPITE???:'))
    tentativas += 1
    if palpite > computador:
        print('ERROU,TENTE DE NOVO...DICA É MENOS')
    elif palpite < computador:
        print('ERROU,TENTE DE NOVO...DICA É MAIS')
    elif computador == palpite:
        acerto = True
print('Acertou ❤')
print(f'VOCÊ PRECISOU DE {tentativas} TENTATIVAS PARA ACERTAR')