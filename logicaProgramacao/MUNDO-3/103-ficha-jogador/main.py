def j(n="desconhecido", g=0):
    print(f"O jogador {n} fez {g} gols.")

nome = input("Nome jogador: ")
gol = input("Número de gols: ")
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip()[:] == '':
    j(g=gol)
else:
    j(nome, gol)