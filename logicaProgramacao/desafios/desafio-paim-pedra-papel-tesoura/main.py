from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador1 = randint(0, 2)
computador2 = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''');
jogador = int(input(('Qual é a sua jogada? ')))
print('Computador jogou {}'.format(itens[computador1]))
print('Computador jogou {}'.format(itens[computador2]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11);
if computador1 == computador2 and computador1 == jogador or computador1 != computador2 and computador1 != jogador:
    print('EMPATE');
elif jogador == 0:
    if computador1 == 0 and computador2 == 1:
        print('Computador 2 GANHOU! Jogador e Computador 1 EMPATARAM!')
    elif computador1 == 0 and computador2 == 2:
         print('Computador 2 PERDEU! Jogador e Computador 1 EMPATARAM!')
    elif computador1 == 1 and computador2 == 0:
        print('Computador 1 GANHOU! Jogador e Computador 2 EMPATARAM!')
    elif computador1 == 2 and computador2 == 0:
        print('Computador 1 PERDEU! Jogador e Computador 2 EMPATARAM!')
elif jogador == 1:
    if computador1 == 0 and computador2 == 0:
        print('Jogador GANHOU! Computador 1 e Computador 2 EMPATARAM!')
    elif computador1 == 0 and computador2 == 1:
        print('Computador 1 PERDEU! Jogador e Computador 2 EMPATARAM!')
    elif computador1 == 0 and computador2 == 2:
        print('EMPATE!')
    elif computador1 == 1 and computador2 == 0:
        print('Computador 2 PERDEU! Jogador e Computador 1 EMPATARAM')
    elif computador1 == 2 and computador2 == 0:
        print('EMPATE!')
    elif jogador == 2:
        if computador1 == 0 and computador2 == 0:
            print('Jogador PERDEU! Computador 1 e Computador 2 EMPATARAM!')
        elif computador1 == 0 and computador2 == 1:
            print('EMPATE!')
        elif computador1 == 0 and computador2 == 2:
            print('Computador 1 GANHOU! Jogador e Computador 2 EMPATARAM!')
        elif computador1 == 1 and computador2 == 1:
            print('EMPATE')
        elif computador1 == 2 and computador2 == 0:
            print('Computador 2 GANHOU! Jogador e Computador 1 EMPATARAM!')
