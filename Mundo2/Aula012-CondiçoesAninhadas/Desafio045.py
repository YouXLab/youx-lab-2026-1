# Crie um programa que faça o computador jogar Jokenpô com vocẽ.
import random

print('''suas opcoes
[0] pedra
[1] papel
[2] tesoura''')

escolhaJogador = int(input('Qual é a sua jogada?'))
escolhaComputador = random.randint(0, 2)
print(escolhaComputador)
if escolhaJogador == escolhaComputador:
    print('Empate')
elif escolhaJogador == 0 and escolhaComputador == 2:
    print('Voce escolheu pedra e o computador escolheu tesoura, VOCE GANHOU!')
elif escolhaJogador == 1 and escolhaComputador == 0:
    print('Voce escolheu papel e o computador escolheu pedra, VOCE GANHOU!')
elif escolhaJogador == 2 and escolhaComputador == 1:
    print('Voce escolheu tesoura e o computador escolheu papel, VOCE GANHOU!')
else:
    print('O computador Ganhou')


