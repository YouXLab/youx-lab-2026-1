numero = int(input('Digite um número: '))
tot = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[34m', end='')
        tot= tot + 1
    else:
        print('\033[m', end='')
    print('{} '.format(c), end='')
print(f"\n\033[m0 O número {numero} foi divisível {tot} vezes")
if tot == 2:
    print('E por isso ele É PRIMO! ')
else:
    print('E por isso ele NÃO É PRIMO')

