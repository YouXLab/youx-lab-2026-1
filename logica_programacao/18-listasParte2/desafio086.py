linha1 = []
linha2 = []
linha3 = []
for valores in range(3):
    for contagem in range(3):
        valor = int(input(f"Digite um valor para {valores, contagem}: "))
        if valores == 0:
            linha1.append(valor)
        elif valores == 1:
            linha2.append(valor)
        elif valores  == 2:
            linha3.append(valor)
#print(matriz)
for valores in linha1:
    print([valores], end =" ")
print()
for valores in linha2:
    print([valores], end =" ")
print()
for valores in linha3:
    print([valores], end =" ")



