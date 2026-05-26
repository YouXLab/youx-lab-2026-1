lista_completa = []
pares = []
impares = []

while True:
    numero = int(input("Digite um número: "))
    lista_completa.append(numero)
    resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input("Resposta inválida. Quer continuar? [S/N] ")).strip().upper()[0]

    if resp == 'N':
        break
for num in lista_completa:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print("-=" * 20)
print(f"Lista completa: {lista_completa}")
print(f"Lista de pares: {pares}")
print(f"Lista de ímpares: {impares}")
