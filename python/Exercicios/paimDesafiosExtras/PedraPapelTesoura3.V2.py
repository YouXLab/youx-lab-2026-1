from random import randint
lista = {'pedra':0, 'papel':0, 'tesoura':0}
jogador = int(input('Suas opções são:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA\nQual sua jogada? '))
computador = {'c1': randint(0, 2), 'c2': randint(0, 2)}
print(f'O computador 1 escolheu {computador["c1"]}')
print(f'O computador 2 escolheu {computador["c2"]}')
print(f'O jogador escolheu {jogador}')
for cont in range(0, 3):
    if jogador == 0: #ganha
        if computador['c1'] == cont and computador['c2'] == cont:
            print(jogador)