numero = int(input('Digite um número: '))
ndivisiveis = 0
for cont in range(1, numero + 1):
    if numero % cont == 0:
        print('\33[33m', end='')
        ndivisiveis += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(cont), end='')
print('\n\033[mO numero {} foi divisível {} vezes'.format(numero, ndivisiveis))
if ndivisiveis == 2:
    print('Então ele é primo!')
else:
    print('Então ele nn é primo!')
    