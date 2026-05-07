cont = 0
soma = 0
numero = int(input('Digite um numero [999 para parar]: '))
print('-=-'*10)
while numero != 999:
    soma += numero
    cont += 1
    numero = int(input('Digite um numero [999 para parar]: '))
    print('-=-' * 10)
print(f'Foram digitado {cont} numero(s) e a soma entre eles e {soma}')