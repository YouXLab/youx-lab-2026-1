N1 = float(input('Digite o primeiro segmento:'))
N2 = float(input('Digite o segundo segmento:'))
N3 = float(input('Digite o terceiro segmento:'))

if N1 < N2 + N3 and N2 < N1 + N3 and N3 < N1 + N2:
    print('Pode formar um triangulo')
else:
    print('Não pode virar um triangulo')