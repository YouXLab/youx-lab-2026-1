def ficha():
    nome = str(input('Nome do jogador: '))
    gols = str(input('Número de gols: '))
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
ficha()