nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))
def ficha(nome=0, gols=0):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

ficha(nome, gols)