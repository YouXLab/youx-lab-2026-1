def ficha(joagdor= '<desconhecido>', gols=0):
    print(f'O jogador {joagdor} fez {gols} gol(s) no campeonato.')

nome = str(input('Nome: '))
gols = str(input('Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome, gols)