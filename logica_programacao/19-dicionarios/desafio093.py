jogador = {}
jogador['nome'] = input('Nome: ')
jogador['partidas'] = int(input('Quantidade de partidas: '))
gols = list()
for i in range(jogador['partidas']):
    print(f'Quantos gols na partida {i+1}? ')
    n_gols = int(input())
    gols.append(n_gols)
    jogador['gols'] = gols
    jogador['total'] = sum(gols)
print('=-' * 90)
print(jogador)
print('=-' * 90)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 90)
print(f'O/A jogador/a {jogador["nome"]} jogou {jogador["partidas"]} partidas')
for k, v in enumerate(gols):
    print(f'Na partida {k+1}, fez {v}')
print(f'Foi um total de {jogador["total"]} gols')









