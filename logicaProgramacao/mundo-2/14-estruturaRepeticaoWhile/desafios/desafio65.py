resposta = 'S'
maior = menor = 0
contador = 0
media = 0
soma = 0
while resposta == 'S':
    numero = int(input('Digite um numero: '))
    soma += numero
    contador += 1
    resposta = str(input('Quer continuar? [S/N] ')).upper()
    if maior == 0 and menor == 0:
        maior = numero
        menor = numero
    elif maior < numero:
        maior = numero
    elif menor > numero:
        menor = numero
    media = soma/contador
print(f'A media dos numeros e {media}, o maior e {maior} e o menor e {menor}')