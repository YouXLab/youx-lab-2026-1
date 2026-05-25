jogador = dict()
partidas = list()
continuar = 'S'
busca = ''
time = list()
while continuar == 'S':
    jogador.clear()
    print('-=' * 10)
    jogador['nome'] = str(input("Digite o nome do jogador: "))
    quant = int(input(f'Digite quantas partidas o {jogador["nome"]} jogou: '))
    partidas.clear()
    for c in range(0, quant):
        partidas.append(int(input(f'Quantos gols na parte {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    continuar = str(input('Deseja continuar [S/N]: ')).upper()[0]
    while continuar not in 'SN':
        print('Esta errado,digite sim ou nao!')
        continuar = str(input('Deseja continuar [S/N]: ')).upper()[0]
if continuar == 'N':
    print('-=' * 20)
    for k,v in enumerate(time):
        print(f'{k:>4}',end=' ')
        for d in v.values():
            print(f'{str(d):<14}',end=' ')
        print()
    print('-=' * 20)

    while busca != '999':
        busca = int(input('Qual jogador voce quer ver os dados [999/S]: '))
        if busca == '999':
            print('ACABOU !!!!')
        elif busca != '999':
            if busca >= len(time):
                print(f'Erro! Nao existe jogador com o codigo {busca}')
            else:
                print(f'LEVANTAMENTO DO JOGADOR {time[busca] ["nome"].upper()}: ')
                for i,g in enumerate(time[busca] ['gols']):
                    print(f'No jogo {i+1} fez {g} gols.')
        print('-=' * 20)
