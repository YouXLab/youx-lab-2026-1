jogadores = list()
jogador = dict()
contador = 0

continuar = ''
while 'N' not in continuar:
    nome = input("Nome do jogador: ")
    partidas = int(input(f"Quantas partidas {nome} jogou? "))
    gols = list()
    for i in range (0 ,partidas):
        gol = int(input(f"Quantos gols na partida {i}?"))
        gols.append(gol)
    jogador = {"cod": contador, "nome": nome, "gols" :gols, "total" :sum(gols)}
    contador += 1
    jogadores.append((jogador.copy()))
    continuar = input("Quer continuar? [S/N] ")
    if continuar != 'S' and continuar != 'N':
        print("Erro! Digite apenas com S ou N")

print("-=" * 30)
for i in jogador.keys():
    print(f"{i:<15}", end="")
print("")
print("-" *60)


