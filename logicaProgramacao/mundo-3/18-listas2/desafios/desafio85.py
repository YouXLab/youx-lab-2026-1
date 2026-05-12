numeros = [[], []]

for n in range(1,8):
    numero = int(input(f'Digite o {n}° numero: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

print(f'Os números pares são: {sorted(numeros[0])}')
print(f'Os números impares são: {sorted(numeros[1])}')