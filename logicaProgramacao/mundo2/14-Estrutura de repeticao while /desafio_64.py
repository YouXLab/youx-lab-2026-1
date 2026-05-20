num = cont = soma = 0
while num != 999:
    num = int(input('Digite um numero [999 para parar]:'))
    soma += num
    cont += 1
print('Voce digitou {} numeros se a soma entre eles foi {}.'.format(cont,soma))