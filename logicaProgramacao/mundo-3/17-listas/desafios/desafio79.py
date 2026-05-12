numeros = []
resposta = 'S'
while resposta == 'S':
    numero = int(input('Digite um número: '))
    if numero not in numeros:
        numeros.append(numero)
        print('Valor adicionado com sucesso...')
    resposta = str(input('Deseja continuar? [S/N] ')).upper()
print(f'Você digitou os números: {numeros}')
