from operator import itemgetter
from random import randint
from time import sleep

jogo= {'jogador1': randint(1,6),
       'jogador2': randint(1,6),
       'jogador3': randint(1,6),
       'jogador4': randint(1,6) }
print('valores sorteados')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
    ranking=sorted(jogo.items(), key=itemgetter(1), )
    for i,v in enumerate(ranking):
        print(f'{i+1} lugar: {v[0]} com {v[1]}')