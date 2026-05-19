lista = [[] , []]
for n in range(1 , 7+1):
    valor = int(input(f"Digite o {n}: "))
    if valor % 2 ==0:
        lista[0].append(valor)
    else:
        lista[2].append(valor)
print(f"Os numeros pares sao {sorted(lista[0])}")
print(f"Os numeros impares sao {sorted(lista[1])}")