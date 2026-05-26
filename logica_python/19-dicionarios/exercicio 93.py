# Dicionário para armazenar os dados do jogador
jogador = {}
partidas = []

# Leitura dos dados básicos
jogador['nome'] = str(input("Nome do Jogador: "))
tot = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

# Leitura dos gols em cada partida
for c in range(0, tot):
    gols = int(input(f"   => Quantos gols na partida {c + 1}? "))
    partidas.append(gols)

# Armazenando a lista de gols e o total no dicionário
jogador['gols'] = partidas
jogador['total'] = sum(partidas)

# Exibição dos resultados
print("-=" * 30)
print(jogador)
print("-=" * 30)

# Exibição detalhada
for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}")

print("-=" * 30)
print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas.")

# Exibição do aproveitamento por partida
for i, g in enumerate(jogador['gols']):
    print(f"   => Na partida {i + 1}, fez {g} gols.")

print(f"Foi um total de {jogador['total']} gols.")
