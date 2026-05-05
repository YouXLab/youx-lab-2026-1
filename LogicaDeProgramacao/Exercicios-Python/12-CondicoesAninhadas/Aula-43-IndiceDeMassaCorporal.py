N1 = float(input('Digite seu peso: '))
N2 = float(input('Digite sua altura: '))
N3 = N1 / (N2 * N2)
if N3 <= 18.5:
    print('Abaixo do Peso')
elif N3 <= 25:
    print('Peso Ideal')
elif N3 <= 30:
    print('Sobrepeso')
elif N3 <= 40:
    print('Obesidade')
elif N3 >= 41:
    print('Obesidade Mórbida')