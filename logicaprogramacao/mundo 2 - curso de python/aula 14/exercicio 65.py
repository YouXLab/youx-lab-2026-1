resp = 'S'
soma = 0
quantidade = 0
media = 0
maior = 0
menor = 0

while resp in 'S':
    numero = int(input('Digite um número: '))
    soma += numero
    quantidade += 1

    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]

media = soma / quantidade
print(f'Você digitou {quantidade} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')