from random import randint
itens = ('Pedra' , 'Papel' , 'Tesoura')
computador1 = randint (0, 2)
computador2 = randint (0, 2)

print('''Suas opções são:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual sua jogador? '))
print('O computador 1 escolheu {}'.format(itens[computador1]))
print('O computador 2 escolheu {}'.format(itens[computador2]))
print('O jogador escolheu {}'.format(itens[jogador]))

if computador1 == computador2 and computador1 == jogador or computador1 != computador2 and computador1 != jogador:
    print('EMPATE!')
elif jogador == 0:  # PEDRA
    if computador1 == 0 and computador2 ==1:
        print('Jogador e Computador 1 EMPATARAM! Computador 2 Ganhou!')
    elif computador1 == 0 and computador2 == 2:
        print('Jogador e Computador 1 EMPATARAM! Computador 2 perdeu!')
    elif computador1 == 1 and computador2 == 0:
        print('Jogador e Computador 2 EMPATARAM! Computador 1 Ganhou!')
    elif computador1 == 2 and computador2 == 0:
        print('Jogador e Computador 2 EMPATARAM! Computador 1 perdeu!')
    elif computador1 == 1 and computador2 == 1:
        print('Computador 1 e Computador 2 EMPATARAM! Jogador perdeu!')
    elif computador1 == 2 and computador2 == 2:
        print('Computador 1 e Computador 2 PERDERAM! Jogador Ganhou!')
elif jogador == 1:  # PAPEL
    if computador1 == 0 and computador2 == 0:
        print('Computador 1 e Computador 2 EMPATARAM! Jogador Ganhou!')
    elif computador1 == 0 and computador2 ==1:
        print('Jogador e Computador 2 EMPATARAM! Computador 1 perdeu!')
    elif computador1 == 1 and computador2 == 0:
        print('Jogador e Computador 1 EMPATARAM! Computador 2 perdeu!')
    elif computador1 == 2 and computador2 == 2:
        print('Computador 1 e Computador 2 EMPATARAM! Jogador perdeu!')
elif jogador == 2: # TESOURA
    if computador1 == 0 and computador2 == 0:
        print('Computador 1 e Computador 2 EMPATARAM! Jogador perdeu!')
    elif computador1 == 0 and computador2 == 2:
        print('Jogador e Computador 2 EMPATARAM! Computador 1 Ganhou!')
    elif computador1 == 2 and computador2 == 0:
        print('Jogador e Computador 1 EMPATARAM! Computador 2 Ganhou!')
    elif computador1 == 1 and computador2 == 1:
        print('Computador 1 e Computador 2 PERDERAM! Jogador Ganhou!')
