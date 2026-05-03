from random import randint
jogadas = {
    "pedra": [],
    "papel": [],
    "tesoura": []
}
pedra = jogadas["pedra"]; papel = jogadas["papel"]; tesoura = jogadas["tesoura"]
jogadores = {
    "jogador 1": randint(1, 3),
    "jogador 2": randint(1, 3),
    "jogador 3": int(input("Digite sua escolha: "))
}
for i in jogadores:
    if jogadores[i] == 1:
        pedra.append(i)
    if jogadores[i] == 2:
        papel.append(i)
    if jogadores[i] == 3:
        tesoura.append(i)
if len(pedra) > 1:
    print(f"Os jogadores {pedra} empataram")
    if papel:
        print(f"E o jogador {papel} ganhou")
    if tesoura:
        print(f"E o jogador {tesoura} perdeu")

if len(papel) > 1:
    print(f"Os jogadores {papel} empataram")
    if pedra:
        print(f"E o jogador {pedra} perdeu")
    if tesoura:
        print(f"E o jogador {tesoura} ganhou")

if len(tesoura) > 1:
    print(f"Os jogadores {tesoura} empataram")
    if pedra:
        print(f"E o jogador {pedra} ganhou")
    if papel:
        print(f"E o jogador {pedra} perdeu")
else:
    print(f"EMPATE!!")