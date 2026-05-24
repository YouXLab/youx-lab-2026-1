
numero = [[], []]
valor = 0
for contagem in range(0, 7):
    valor = int(input('Digite seu valor: '))
    if valor % 2 == 0:
        numero[0].append(valor)
    else:
        numero[1].append(valor)
print(f'Os valores pares sao: {numero[0]}')
print(f'Os valores impares sao: {numero[1]}')