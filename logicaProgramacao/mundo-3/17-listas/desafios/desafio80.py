numeros = []
for c in range(0,5):
    valor = int(input('Digite um número: '))
    if c == 0:
        numeros.append(valor)
    else:
        if valor < numeros[0]:
            numeros.insert(0, valor)
        elif valor > numeros[0]:
          numeros.insert(c+1, valor)
print(numeros)