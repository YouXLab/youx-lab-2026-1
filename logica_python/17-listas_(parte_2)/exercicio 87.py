matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = maior = somacoluna3 = 0

matriz[0][0] = int(input("Digite um valor para [0, 0]: "))
matriz[0][1] = int(input("Digite um valor para [0, 1]: "))
matriz[0][2] = int(input("Digite um valor para [0, 2]: "))

matriz[1][0] = int(input("Digite um valor para [1, 0]: "))
matriz[1][1] = int(input("Digite um valor para [1, 1]: "))
matriz[1][2] = int(input("Digite um valor para [1, 2]: "))

matriz[2][0] = int(input("Digite um valor para [2, 0]: "))
matriz[2][1] = int(input("Digite um valor para [2, 1]: "))
matriz[2][2] = int(input("Digite um valor para [2, 2]: "))

todas_as_caixas = [
    matriz[0][0], matriz[0][1], matriz[0][2],
    matriz[1][0], matriz[1][1], matriz[1][2],
    matriz[2][0], matriz[2][1], matriz[2][2]
]
for numero in todas_as_caixas:
    if numero % 2 == 0:
        somapares += numero

somacoluna3 = matriz[0][2] + matriz[1][2] + matriz[2][2]

maior = max(matriz[1][0], matriz[1][1], matriz[1][2])

print("-=" * 30)
print(f"[{matriz[0][0]:^5}][{matriz[0][1]:^5}][{matriz[0][2]:^5}]")
print(f"[{matriz[1][0]:^5}][{matriz[1][1]:^5}][{matriz[1][2]:^5}]")
print(f"[{matriz[2][0]:^5}][{matriz[2][1]:^5}][{matriz[2][2]:^5}]")
print("-=" * 30)

print(f"A) A soma de todos os valores pares digitados é {somapares}.")
print(f"B) A soma dos valores da terceira coluna é {somacoluna3}.")
print(f"C) O maior valor da segunda linha é {maior}.")
