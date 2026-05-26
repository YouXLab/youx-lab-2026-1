# CADASTRO DE JOGADORES
# Lista + Dicionário + FOR

time = []

for i in range(2):
    jogador = {}
    gols = []

    jogador["nome"] = input("\nNome do jogador: ")

    partidas = int(input("Quantas partidas jogou? "))

    total = 0

    for c in range(partidas):
        gol = int(input(f"Gols na partida {c+1}: "))
        gols.append(gol)
        total += gol

    jogador["gols"] = gols
    jogador["total"] = total

    time.append(jogador)

print("\nRELATÓRIO")
print("-" * 40)

for j in time:
    print(f"Jogador: {j['nome']}")
    print(f"Gols: {j['gols']}")
    print(f"Total de gols: {j['total']}")
    print("-" * 40)