def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do Fatorial de um número n
    """
    fatorial = n
    for f in range(n-1, 0, -1):
        fatorial *= f
    if show == True:
        print(f'{n}', end=' ')
        for f in range(n-1, 0, -1):
            print(f'x {f}', end=' ')
        print('', end='')
        print(f'= {fatorial}')
        print('')
    else:
        print(fatorial)
fatorial(5)
help(fatorial)