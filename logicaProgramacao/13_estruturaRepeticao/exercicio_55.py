maior= 0
menor= 0
for p in range(1,6):
    peso= float(input(f'digite seu {p}ª peso: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O maior peso é {maior}')
print(f'O menor peso é {menor}')
