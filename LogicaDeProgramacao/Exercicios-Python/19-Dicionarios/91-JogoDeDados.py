from operator import itemgetter
from random import randint
jogos = {'jogador [1]': randint(1,6),
         'jogador [2]': randint(1,6),
         'jogador [3]': randint(1,6),
         'jogador [4]': randint(1,6)}
print('Valores sorteados:')
for a,b in jogos.items():
    print(f'{a} tirou {b} no dado')
ranking = sorted(jogos.items(),key=itemgetter(1),reverse=True)
print('-='*30)
print(' '*13,'== Ranking Dos Jogadores ==')
for a,b in enumerate(ranking):
    print(' '*13,f'{a+1} Lugar: {b[0]} com {b[1]}')