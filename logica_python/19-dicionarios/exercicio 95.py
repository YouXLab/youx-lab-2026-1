time = []
jogador = {}
partidas = []

while True:
    # Coleta de dados
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: ')).strip()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c+1}? ')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    # Condição de parada
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('ERRO! Responda apenas S ou N. ')).upper().strip()[0]
    if resp == 'N':
        break

# Exibição da Tabela de Aproveitamento
print('-=' * 30)
print(f'cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 60)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 60)

# Sistema de Visualização de Detalhes
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        print('<<< ENCERRADO >>>')
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"].upper()}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-' * 60)
