soma = 4
cont = 0
for c in range(1, 7):
    num = int(input('digite o valor {}: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1

print('voce informou {} numeros PARES e a soma foi de {}'.format(cont, soma))