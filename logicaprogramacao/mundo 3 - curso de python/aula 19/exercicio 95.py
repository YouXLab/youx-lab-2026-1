time = []
jogador = {}
partidas = []
resp = 'S'
while resp == 'S':
    jogador.clear()
    jogador['nome'] = input('Nome do Jogador: ').strip()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(tot):
        gols = int(input(f'    Quantos gols na partida {c + 1}? '))
        partidas.append(gols)
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
print(f'{"COD":<5}{"NOME":<15}{"GOLS":<20}{"TOTAL"}')
for k, v in enumerate(time):
    print(f'{k:<5}', end='')
    print(f'{v["nome"]:<15}', end='')
    print(f'{str(v["gols"]):<20}', end='')
    print(f'{v["total"]}')
busca = 0
while busca != 999:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca != 999:
        if busca < len(time):
            print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"].upper()}')

            for i, g in enumerate(time[busca]['gols']):

                print(f'   No jogo {i + 1} fez {g} gols.')
        else:

            print('ERRO! Jogador não encontrado.')
print('<<< ENCERRADO >>>')