completa = [[], []]

for c in range(1, 8):
    valor = int(input(f"Digite o {c}º valor: "))
    if valor % 2 == 0:
        completa[0].append(valor)
    else:
        completa[1].append(valor)

completa[0].sort()
completa[1].sort()

# Exibe os resultados
print("-=" * 20)
print(f"Valores pares em ordem crescente: {completa[0]}")
print(f"Valores ímpares em ordem crescente: {completa[1]}")
