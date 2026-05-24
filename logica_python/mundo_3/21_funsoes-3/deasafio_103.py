def ficha(nome, gols):
    (print(f'o jogador {nome} fez {gols} gol(s).'))
    n = input('nome: ')
    g =   input('gols: ')
    if g.isnumeric():
         g = int(g)
    else:
         g = 0
    if n == '':
        n = 'desconhecido'
        ficha(n, g)