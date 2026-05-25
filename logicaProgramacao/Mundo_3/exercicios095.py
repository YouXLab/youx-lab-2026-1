#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização
#de detalhes do aproveitamento de cada jogador.

time = []

for c in range(int(input('Quantos jogadores? '))):
    jogador = {}
    gols = []

    jogador['nome'] = input('Nome: ')
    partidas = int(input('Partidas: '))

    for i in range(partidas):
        gols.append(int(input(f'Gols na partida {i+1}: ')))

    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    time.append(jogador)
    print('\nCOD  NOME      GOLS       TOTAL')
for i, j in enumerate(time):
    print(i, j['nome'], j['gols'], j['total'])
busca = int(input('\nMostrar dados de qual jogador? '))
print(f'\nLevantamento de {time[busca]["nome"]}')
for i, g in enumerate(time[busca]['gols']):
    print(f'No jogo {i+1} fez {g} gols.')