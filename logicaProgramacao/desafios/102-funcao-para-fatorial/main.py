def fatorial(n, show=False):
    '''
    -> Calcula o Fatorial de um número
    :param n:O número a ser calculado.
    :param show:(opcional) Mostrar ou não a conta.
    :return:O valor do Fatorial de um número n.
    '''
    fator = n
    for i in range(n-1, 0, -1):
        fator *= i
    if show == True:
        print(f'{n}', end='')
        for i in range(n-1, 0, -1):
            print(f' x {i}', end='')
        print('', end='')
        print(f' = {fator}')
        print('')
    elif show == False:
        print(fator)


fatorial(5, True)
help(fatorial)