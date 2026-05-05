from time import sleep

while True:
    N1 = int(input('Digite um numero para a tabuada [Numero negativa para acabar]'))
    if N1 < 0:
        break

    T1 = N1 * 1
    T2 = N1 * 2
    T3 = N1 * 3
    T4 = N1 * 4
    T5 = N1 * 5
    T6 = N1 * 6
    T7 = N1 * 7
    T8 = N1 * 8
    T9 = N1 * 9
    T10 = N1 * 10

    print('-----------------')
    print(N1, 'x  1 =', T1)
    print(N1, 'x  2 =', T2)
    print(N1, 'x  3 =', T3)
    print(N1, 'x  4 =', T4)
    print(N1, 'x  5 =', T5)
    print(N1, 'x  6 =', T6)
    print(N1, 'x  7 =', T7)
    print(N1, 'x  8 =', T8)
    print(N1, 'x  9 =', T9)
    print(N1, 'x 10 =', T10)
    print('-----------------')

print('Finalizando.', end= '')
sleep(1)
print('.', end='')
sleep(1)
print('.')
sleep(1)
print('==================//====================')
print('Fim.')
input()