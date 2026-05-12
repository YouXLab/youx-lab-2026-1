import random
import time
from operator import itemgetter

jogadores = {'jogador1': random.randint(1, 6), 'jogador2': random.randint(1, 6), 'jogador3': random.randint(1, 6), 'jogador4': random.randint(1, 6)}
print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'   O {k} tirou {v}')
    time.sleep(1)
ordem = sorted(jogadores.items())
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores:')
for i, v in enumerate(ranking):
    print(f'   {i+1}° lugar: {v[0]} com {v[1]}.')
    time.sleep(1)