posicao1 = []
totPos1 = []
posicao2 = []
totPos2 = []
posicao3 = []
totPos3 = []
contador = 1

for i in range(3):
    posicao1.append(int(input(f'Digite um numero para a posição [1, {i}]: ')))
    totPos1.append(posicao1[:])
    posicao1.clear()
for i in range(3):
    posicao2.append(int(input(f'Digite um numero para a posição [2, {i}]: ')))
    totPos2.append(posicao2[:])
    posicao2.clear()
for i in range(3):
    posicao3.append(int(input(f'Digite um numero para a posição [3, {i}]: ')))
    totPos3.append(posicao3[:])
    posicao3.clear()
print('-='*30)
for i in totPos1:
    print(f'{i}',end=' ')
print()
for i in totPos2:
    print(f'{i}',end=' ')
print()
for i in totPos3:
    print(f'{i}',end=' ')
print()
