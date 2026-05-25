numero=[[], []]
valores=0
for c in range(1,8):
    valores =int(input(f'digite um valor: '))
    if valores % 2 == 0:
        numero[0].append(valores)
    else:
        numero[1].append(valores)
numero[0].sort()
numero[1].sort()
print(f'os valores pares digitados foram {numero[0]}')
print(f'os valores impares digitaddos foram{numero[1]}')










