maior = 0
menor = 0
for pesog in range(1, 6):
    peso = float(input('Digite o peso da {}º pessoa: '.format(pesog)))
    if pesog == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso registrado é {}Kg'.format(maior))
print('O menor peso registrado é {}Kg'.format(menor))
