numero = int(input('digite um numero:'))
fatorial = 1
for c in range(numero, 0, -1):
    fatorial *= c
print(f'o fatorial de {numero} é {fatorial}')
