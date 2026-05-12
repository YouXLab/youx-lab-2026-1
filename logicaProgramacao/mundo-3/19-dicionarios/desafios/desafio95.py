resposta = 'S'
jogadores = []

while resposta =='S':
    print('-'*28)
    dados = {}
    gol_partida = []
    total_gols = 0
    dados['jogador'] = str(input('Nome: '))
    partidas = int(input(f'Quantas partidas {dados['jogador']} jogou? '))
    for g in range(0, partidas):
        gol = int(input(f'Gols na partida {g + 1}? '))
        gol_partida.append(gol)
        total_gols += gol
    dados['gols'] = gol_partida
    dados['total'] = total_gols
    jogadores.append(dados)
    resposta = str(input('Quer continuar? [S/N] ')).upper()
    while resposta not in 'SN':
        print('Resposta inválida. Tente novamente.')
        resposta = str(input('Quer continuar? [S/N] ')).upper()

print('-='*30)
print(f'{'Cod.'} {'Jogador':<10} {'Gols':^8} {'Total'}')
for c in range(0, len(jogadores)):
    print(f'{c} {jogadores[c]['jogador']:<10} {jogadores[c]['gols']} {jogadores[c]['total']}')
mostrar = 1
while mostrar != 999:
    mostrar = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    print(f'Levantamento do jogador {jogadores[mostrar]['jogador']}:')
    for p in range(0, len(jogadores[mostrar]['gols'])):
        print(f'No jogo {p+1} fez {jogadores[mostrar]['gols'][p]}')