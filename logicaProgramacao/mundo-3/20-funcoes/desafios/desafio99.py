import time


def maior(*valores):
    print('Analizando valores passados...')
    maior = 0
    for n in valores:
        print(n, end=' ')
        print('', end='')
        time.sleep(0.25)
    print(f'Foram informados {len(valores)} valores ao todo')
    for n in valores:
        if n == 0:
            maior = n
        elif n > maior:
            maior = n
    print(f'O maior valor informado foi {maior}')

maior(1, 4, 7, 9)
maior(12, 87, 123, 4, 9, 15, )
maior(5, 1)