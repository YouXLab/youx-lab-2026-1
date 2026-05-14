soma = 0
contador = 0
maior = 0
menor = 0
continuar = 'S'
while continuar == 'S':
    numero = int(input('Digite um número inteiro: '))
    soma += numero
    contador += 1
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = soma / contador
print("-" * 30)
print(f"Você digitou {contador} números.")
print(f"A média foi {media:.2f} ")
print(f"O maior valor foi {maior} e o menor foi {menor} ")
print("=" * 30)




