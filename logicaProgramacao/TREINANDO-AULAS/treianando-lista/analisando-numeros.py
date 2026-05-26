# ANALISANDO NÚMEROS
# Lista + FOR + condições

numeros = []
pares = []
impares = []

for i in range(5):
    n = int(input(f"Digite o {i+1}° número: "))
    numeros.append(n)

for valor in numeros:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print("-" * 30)
print(f"Lista completa: {numeros}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")