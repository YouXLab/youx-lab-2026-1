numero = []
pares = []
impares = []
resp = 'S'
while resp != 'N':
    numero.append(int(input('Digite um número: ')))
    resp = input('Quer continuar? [S/N] ').strip().upper()
for n in numero:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'A lista completa é {numero}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')