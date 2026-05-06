#Maior e menor da sequencia

maior = 0
menor = 1000
for c in range(1, 5):
    peso = int(input(f"Digite o peso da pessoa numero {c}: "))
    if peso > maior:
        maior = peso

    if peso < menor:
        menor = peso

print(f"O maior peso é {maior}")
print(f"O menor peso é {menor}")