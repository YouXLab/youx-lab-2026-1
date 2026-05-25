matriz=[[0,0,0], [0,0,0],[0,0,0]]
spar = mai = scol=0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c]= int(input(f'digite um valor para [{l} , {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end=' ')
        spar += matriz[l][c]
    print()
print(f'a soma dos valores é {spar}' )
for l in range(0,3):
    scol += matriz[l][2]
print(f'a soma dos valores da terciera coluna é {scol}')
for c in range(0 , 3):
    if c == 0:
        mai= matriz[1][c]
    elif matriz[1][c]> mai:
        mai=matriz[1][c]
print(f'o maior valor da segunda linha é {mai}')