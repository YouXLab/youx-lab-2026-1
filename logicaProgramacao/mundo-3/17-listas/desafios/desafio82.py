numeros = []
pares = []
impares = []
resposta = 'S'
while resposta == 'S':
    numeros.append(int(input('Digite um número: ')))
    resposta = str(input('Deseja continuar? [S/N] ')).upper()
    while resposta not in'NS':
        print('Resposta inválida. Tente novamente.')
        resposta = str(input('Deseja continuar? [S/N] ')).upper()
for n in range(0,len(numeros)):
    if numeros[n] % 2 == 0:
        pares.append(numeros[n])
    else:
        impares.append(numeros[n])
print(f'Você digitou os números: {numeros}')
print(f'Os números pares são: {pares}')
print(f'Os números impares são: {impares}')