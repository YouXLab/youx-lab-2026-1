soma = 0
contador = 0
for numeros in range(1, 501, 2):
    if numeros % 3 == 0:
        contador = contador + 1
        soma = soma + numeros
print('A soma dos {} valores é igual a {}'.format(contador, soma))