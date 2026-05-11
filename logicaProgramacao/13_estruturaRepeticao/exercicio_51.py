termo =int(input('primeiro termo'))
razao= int(input('razao'))
decimo = termo + 10-1 * razao
for c in range(termo, decimo + razao, razao):
    print(f'{c}', end= ' ')