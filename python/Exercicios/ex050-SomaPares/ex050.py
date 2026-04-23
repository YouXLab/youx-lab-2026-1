soma = 0
cont = 0
for contador in range(1, 7):
    numero = int(input('Digite o {} número: '.format(contador)))
    if numero % 2 == 0:
        soma = soma + numero
        cont += 1
print('A soma dos {} números PARES escolhidos é: {}'.format(cont, soma))