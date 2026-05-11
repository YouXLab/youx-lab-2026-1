resposta = 'S'
soma = 0
maior = 0
menor = 0
contador = 0



while resposta != 'N':
    numero = int(input('Digite seu numero para a media: '))
    soma += numero
    if contador == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    contador += 1


    resposta = str(input('Voce quer continuar? [S/N] ')).upper()

media = soma / contador
print(media)
print(f'O maior numero e {maior} e o menor numero e {menor}')
