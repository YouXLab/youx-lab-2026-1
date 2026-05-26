def ficha(nome='<desconhecido>', gols=0):
    """Mostra a ficha de um jogador, tratando valores ausentes ou inválidos."""
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


# Programa Principal
n = str(input("Nome do Jogador: "))
g = str(input("Número de Gols: "))

# Verifica se a entrada de gols é um número válido
if g.isnumeric():
    g = int(g)
else:
    g = 0

# Verifica se o nome foi deixado em branco
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
