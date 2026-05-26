#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogadores = []
jogador = {}
contador = 0

continuar = ''
while continuar != 'N':
    nome = input("Nome do jogador: ")
    partidas = int(input(f"Quantas partidas {nome} jogou? "))
    gols = []
    for indice in range(1, partidas):
        gol= int(input(f"Quantos gols ele fez na {indice}"))
        gols.append(gol)
    jogador = {'cod': contador,
               'nome':nome,
               'gols':gols,
               'total': sum(gols)
               }
    contador += 1
    jogadores.append(jogador.copy())
    continuar = input("Quer continuar: [S/N]").upper()
    while 'SN' not in continuar:
        continuar = input("Erro! Digite apenas ")
    for indice in jogador.keys():
        print(f'{indice:<15}',end="")
    print()
    print('-'*50)
    for indice, jogador in enumerate(jogadores):
        for dados in jogador.values():
            print(f"{str(dados):<15 }", end ="")
        print()
    print('-'*50)
    continuar_jogador ='S'
    while continuar_jogador != 'N':
        codigo = int(input("Quer ver os dados de qual jogador? "))
        if codigo ==999:
            print("VOLTE SEMPRE")
        continuar_jogador = 'N'
        for
