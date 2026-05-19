#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que
# agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.


from random import randint
from time import sleep
computador = randint (0 , 10)
print('Escolha um número entre 0 e 10')
print('Vou pensar em um número entre 0 e 10,tente adivinhe qual número pensei')
jogador = int(input('Em que número eu pensei? '))
acertou = False
palpite = 0
while not acertou:
    jogador = int(input("Você errou.Tente denovo:  "))
    palpite += 1
    if jogador == computador:
        acertou = True
print(f"parabéns!.Você deu {palpite} palpites ")
