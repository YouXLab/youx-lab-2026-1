jogador={}
gols=[]
total=0
jogador['nome'] = input('nome do jogador: ')
partidas= int(input('quantas partidas ele jogou? '))
for c in range(partidas):
    gol=(int(input(f'gols na partida {c+1}: ')))
    gols.append(gol)
    total += gol
jogador['gols'] = gols
jogador['total']= total
print(jogador)
