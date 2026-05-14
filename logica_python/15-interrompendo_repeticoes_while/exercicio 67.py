while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 20)

    # Verifica se o número é negativo para parar
    if n < 0:
        break

    # Gera a tabuada de 1 a 10
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 20)

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

