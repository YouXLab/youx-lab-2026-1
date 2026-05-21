jogador = dict()
gols = list()
jogador['Nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))
for a in range(1,tot+1):
    gols.append(int(input(f'Quantos gols foram feitos na partida {a}? ')))
jogador['Gols'] = gols[:]
jogador['Total'] = sum(gols)
print('-='*30)
print(jogador)
print('-='*30)
for a,b in jogador.items():
    print(f'O campo {a} tem o valor de {b}')
print('-='*30)
print(f'O jogador {jogador['Nome']} jogou {len(jogador['Gols'])} partidas.')
for a,b in enumerate(jogador['Gols']):
    print(f'Na partida {a}, fez {b} gols')
print(f'Foi um total de {jogador['Total']} gols')




