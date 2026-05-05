N1 = int(input('Digite um numero para ver seu calculo fatoral: '))
P1 = N1
P2 = 1
while P1 >= 1:
    P2 *= P1
    P1 -= 1
    print(f'{P1} ',end='')
    print(' x ' if P1 > 1 else ' = ',end=' ')

print(f'O fatorial de {N1} é {P2}')
