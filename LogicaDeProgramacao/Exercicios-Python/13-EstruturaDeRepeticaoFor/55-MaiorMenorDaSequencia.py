# pesos = [ ]
# for p in range(0,5):
#     peso = float(input('Digite o peso: '))
#     pesos.append(peso)
# print(f'O maior peso é {}Kg' .format(max(pesos)))
# print(f'O menor peso é {}Kg' .format(min(pesos)))

maior = 0
menor = 0

for p in range (0, 5):
    peso = float(input("Digite o peso: "))
    if p == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior =peso
        if peso < menor:
            menor = peso

print(f'O maior peso é {maior}Kg')
print(f'O menor peso é {menor}Kg')
