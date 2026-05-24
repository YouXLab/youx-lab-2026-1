pessoas = []
maior = menor = 0
resp = 'S'

while resp != 'N':
    nome = input('Nome: ')
    peso = float(input('Peso: '))

    pessoas.append([nome, peso])

    if len(pessoas) == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

    resp = input('Quer continuar? [S/N] ').upper()

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')

print(f'O maior peso foi {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')

print()

print(f'O menor peso foi {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')