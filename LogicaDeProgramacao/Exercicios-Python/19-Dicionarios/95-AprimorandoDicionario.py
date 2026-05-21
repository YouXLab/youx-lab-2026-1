from operator import itemgetter
jogador = dict()
gols = list()
jogador['Nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))
for a in range(1,tot+1):
    gols.append(int(input(f'Quantos gols foram feitos na partida {a}? ')))
jogador['Gols'] = gols[:]
jogador['Total'] = sum(gols)
N = int(input('Deseja ver o jogo de qual jogador? [-1 interrompe]: '))
while N != -1:
    for i, a in enumerate(jogador):
        if i == N:
            print(f'Notas de {a[0]} são: {a[1]}')
    N = int(input('Deseja ver o jogo de qual jogador? [-1 interrompe]: '))