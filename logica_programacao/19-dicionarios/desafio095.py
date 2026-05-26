time = list()
while True :
    jogador = dict()
    gols_por_partida = list()
    gols = 0
    jogador['nome'] = str(input('Qual o nome do jogador: '))
    partida = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    for c in range(1,partida+1) :
        gols_por_partida.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {c}: ')))
        gols =sum(gols_por_partida)
    jogador['gols'] = gols_por_partida[:]
    jogador['total'] = gols
    time.append(jogador.copy())
    while True:
        continuar = str(input('Deseja adicionar mais algum jogador?[S/N]')).upper()
        if continuar != 'S' and continuar != 'N':
            print('ERRO. Por favor, digite S para sim ou N para não continuar.')
        else:
            break
    if continuar  != '' and continuar == 'N':
        break
print(f'|{"COD":<5} | {"Nome":<25} | {"Gols por partida":>25} | {"Total":>10}|')

for i,j in enumerate(time):
    print(f'|{i:<5} | {j["nome"]:<25} | {str(j["gols"]):>25} | {j["total"]:>10}|')
while True :
    while True:
        codigo = int(input('Digite o código do jogador que quer ver mais detalhes: [999 para  sair.]'))
        if codigo == 999 :
            break
        if codigo < 0 or codigo >= len(time):
            print('ERRO. Digite um código valido')
        else:
            break
    if codigo == 999 :
            break
    jogador = time[codigo]
    print(f'LEVANTAMENTO DO JOGADOR {jogador["nome"]}')
    for k,v in enumerate (jogador['gols']) :
        if v <= 1:
            print(f'No jogo {k+1} {jogador["nome"]} fez {v} gol')
        else:
            print(f'No jogo {k+1} {jogador["nome"]} fez {v} gols')
        print()
    print('......')

print('Programa encerradooooo......')