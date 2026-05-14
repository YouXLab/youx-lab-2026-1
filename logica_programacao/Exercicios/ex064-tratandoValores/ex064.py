cont=1
soma = 0
numero=int(input('digite um numero:'))
while numero != 999:
    numero=int(input('digite um numero:'))
    cont +=1
    soma += numero
print(f'voce digitou {cont} e soma entre eles foi {soma-999}')