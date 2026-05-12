jogador = {}
gol_partida = []
total_gols = 0
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
for g in range(0, partidas):
    gol = int(input(f'Gols na partida {g+1}? '))
    gol_partida.append(gol)
    total_gols += gol
jogador['gols'] = gol_partida
jogador['total'] = total_gols
for c, v in jogador.items():
    print(f'O campo {c} tem o valor {v}')
print(f'O jogador {jogador['nome']} jogou {partidas} partidas.')

for p in range(0, len(gol_partida)):
    print(f'=> Na partida {p+1}, fez {gol_partida[p]}.')