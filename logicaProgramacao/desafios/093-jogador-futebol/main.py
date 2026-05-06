jogador = {"nome": input("Nome do jogador: "),
    "gols": [],
    "total": 0}
for i in range(0, int(input(f"Quantas partidas {jogador['nome']} jogou?: "))):
    gols1 = int(input(f"   Quantos gols {jogador['nome']} fez na partida {i+1}: "))
    jogador["gols"].append(gols1)
    jogador["total"] += gols1
print("--"*25)
print(jogador)
print("--"*25)
for n, v in jogador.items():
    print(f"O campo {n} tem o valor {v}")
print("--"*25)
print(f"O jogador {jogador['nome']} jogador jogou {len(jogador['gols'])} partidas!")
for i, e in enumerate(jogador["gols"]):
    print(f"   => Na partida {i+1}, fez {e} gols.")
print(f"Foi um total de {jogador['total']} gols.")