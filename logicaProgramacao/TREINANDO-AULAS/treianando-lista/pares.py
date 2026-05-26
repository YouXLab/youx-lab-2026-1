# CONTANDO valores pares na lista
numeros = [1, 2, 3, 4, 5, 6]
pares = 0

for n in numeros:
    if n % 2 == 0:
        pares += 1

print(f"Tem {pares} números pares")