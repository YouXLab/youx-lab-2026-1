from random import randint
itens = ('Pedra' , 'Papel' , 'Tesoura')
computador = randint (0, 2)

print('''Suas opções são:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogada = int(input('Qual sua jogada? '))
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogada]))

if computador == 0: #PEDRA
    if jogada == 0:
        print('Empate!')
    elif jogada == 1:
        print('Jogador ganhou!')
    elif jogada == 2:
        print('Jogador perdeu!')
    else:
        print('Jogada inválida!')

elif computador == 1: #PAPEL
    if jogada == 0:
        print('Jogador perdeu!')
    elif jogada == 1:
        print('Empate!')
    elif jogada == 2:
        print('Jogador ganhou!')
    else:
        print('Jogada inválida!')

elif computador == 2: #TESOURA
    if jogada == 0:
        print('Jogador ganhou!')
    elif jogada == 1:
        print('Jogador perdeu!')
    elif jogada == 2:
        print('Empate!')
    else:
        print('Jogada inválida!')
