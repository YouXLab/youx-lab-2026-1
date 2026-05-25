jogador = dict()
partidas = list()
jogador['nome'] = str(input("Digite o nome do jogador: "))
quant = int(input(f'Digite quantas partidas o {jogador["nome"]} jogou: '))
for c in range (0,quant):
    partidas.append(int(input(f'Quantos gols na parte {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(jogador)
print('-='*10)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor de {v}')
print('-='*10)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} vezes')
for i,v in enumerate(jogador["gols"]):
    print(f'==> Na partida {i},fez {v} gols')
print(f'Foi um total de {jogador['total']} gols')