# mostrar um menu com as tres opcoes do jokenpo
#ler a opcao do usoario
#fazer o computador gerar um numero entre um e tres conrrespondente as opcoes do jonkempo
#fazer a comparacao das opcos que o putador fez com a opcao do jogador(fazer comparacao com varios if)
import random

print('''suas opçoes
[0] pedra
[1] papel
[2]tesoura''')

escolhaJogador = int(input('qual sua jogada?'))
escolhaComputador = random.randint(0, 2)
print('escolhaComputador')
if escolhaJogador == escolhaComputador:
    print('empate')
elif escolhaJogador == 0 and escolhaComputador == 2:
    print('voce escolheu pedra e o computador escolheu tesoura, VOCE GANHOU!')
elif escolhaJogador == 1 and escolhaComputador == 0:
    print('voce escolheu papel e o computador escolheu  pedra, VOCE GANHOU!')
elif escolhaJogador == 2 and escolhaComputador== 1:
    print('voce escolheu tesoura e o computador escolheu papel, VOCE GANHOU!')
else:
    print('o computadou GANHOU!')