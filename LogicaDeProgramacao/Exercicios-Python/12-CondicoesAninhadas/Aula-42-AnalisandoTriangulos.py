N1 = float(input('Primeiro segmento: '))
N2 = float(input('Segundo segmento: '))
N3 = float(input('Terceiro segmento: '))

if N1 == N2 == N3:
    print('EQUILATERO')
elif N1 == N2 and N1 != N3 or N2 == N3 and N2 != N1 or N3 == N1 and N3 != N2:
    print('ISOCELES')
elif N1 != N2 and N1 != N3 and N2 != N3:
    print('ESCALENO')
else:
    print('ERRO')