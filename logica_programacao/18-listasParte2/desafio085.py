numero = [[], []] #lista 0 e 1 respectivamente
valor = 0
for contagem in range(1, 8):
    valor = int(input(f"Diga o {contagem}° número:"))
    if valor % 2 == 0:
        numero[0].append(valor)
    else:
        numero[1].append(valor)
print("-=-"*30)
print(f"Os valores pares digitados foram: {numero[0]} ")
print(f"Os valores ímpares digitados foram: {numero[1]}")
print("-=-"*30)








