numeros = []
resposta = 'S'
while resposta == 'S':
    numeros.append(int(input('Digite um numero: ')))
    resposta = str(input('Deseja continuar? [S/N] ')).upper()
print(f'Você digitou {len(numeros)} números.')
print(f'Lista em ordem decrescente: {sorted(numeros, reverse=True)}')
if 5 in numeros:
    print(f'Você digitou no número 5.')
else:
    print('Você não digitou o número 5.')