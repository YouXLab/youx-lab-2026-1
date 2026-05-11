
from random import randint
from time import sleep
computador = randint(0, 10)
print('Pensei em numeros entre 0 a 10, tente adivinhar')
acertou = False
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    if jogador == computador:
        acertou = True
print('ACERTOU!!!!!!!!!!! ')

