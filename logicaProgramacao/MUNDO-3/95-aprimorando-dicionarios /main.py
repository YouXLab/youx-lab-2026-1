print("-" * 24)
print("  CADASTRO JOGADORES")
print("-" * 24)

dicionario = {}
lista = []

continuar = "S"

while continuar in "Ss":

    n = input("Nome: ").strip()

    p = int(input(f"Quantas partidas {n} jogou?: "))

    gols = []
    total = 0

    for i in range(0, p):
        gi = int(input(f"  Quantos gols {n} fez na partida {i+1}?: "))
        gols.append(gi)
        total += gi

    dicionario["nome"] = n
    dicionario["gols"] = gols
    dicionario["total"] = total

    lista.append(dicionario.copy())

    dicionario.clear()

    continuar = input("Deseja continuar? [S/N]: ").strip()[0]

    while continuar not in "SsNn":
        print("Opção inválida! Use S ou N")
        continuar = input("Deseja continuar? [S/N]: ").strip()[0]

    print("-" * 25)

print("-=" * 25)

print(f"{'Cod':<4} {'Nome':<10} {'Total':<15} {'Gols'}")
print("-" * 40)

for i in lista:
    print(f"{lista.index(i)+1:<4} {i['nome']:<10} {i['total']:<15} {i['gols']}")

op = 0

while op != 999:

    op = int(input("Mostrar dados de qual jogador? (999 para sair): "))

    if op != 999:

        if 1 <= op <= len(lista):

            print(f"-- LEVANTAMENTO DO JOGADOR {lista[op-1]['nome']} --")

            for n, v in enumerate(lista[op-1]["gols"]):
                print(f"  No jogo {n+1} fez {v} gols.")

        else:
            print(f"Jogador inválido! Digite um código de 1 até {len(lista)}")