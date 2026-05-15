soma = 0
quantidade = 0
resposta ='S'
while resposta == 'S':
    numero = int(input('digite um numero:'))
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    resposta = input('voce quer continuar?[S/N]').upper()
    media = soma /quantidade
    print(f'a media foi{media}')
    print(f'o maior valor foi {maior}')
    print(f' o menor valor {menor}')