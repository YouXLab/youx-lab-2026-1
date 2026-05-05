from random import randint
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas opcoes sao:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual a sua jogada? ' ))
print ('-=' *11)
print (f'Jogador jogou {itens[jogador]}')
print (f'Computador jogou {itens[computador]}')
print ('-=' *11)