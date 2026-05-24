jogador = {}
partidas = []
jogador['nome'] = input('Nome do jogador: ')
total = int(input('Quantas partidas o jogador jogou no total? '))
for c in range(0, total):
    partidas.append(int(input(f'   Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
print(jogador)