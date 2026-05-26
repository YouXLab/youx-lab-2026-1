from random import randint
from time import sleep
from operator import itemgetter
jogadores = {
    'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6)
}

print('VALORES SORTEADOS')
for k, v in jogadores.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(0.5)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('\nRANKING DOS VENCEDORES')
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]} pontos.')
    sleep(0.5)