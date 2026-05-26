from random import randint
from time import sleep
from operator import itemgetter

# Dicionário para armazenar os resultados
jogo = {
    'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6)
}

ranking = list()

print('=== VALORES SORTEADOS ===')
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1) # Pausa de 1 segundo entre cada jogada

# Ordena o dicionário pelo valor do dado (itemgetter(1)), de forma decrescente (reverse=True)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('\n=== RANKING DOS JOGADORES ===')
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]} pontos.')
    sleep(1)
