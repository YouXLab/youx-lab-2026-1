#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema
# de visualização de detalhes do aproveitamento de cada jogador.


time = list()
jogador = dict()
partidas = list()

resp = 'S'
while resp == 'S':
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp not in 'SN':
            print('ERRO! Responda apenas S ou N.')

