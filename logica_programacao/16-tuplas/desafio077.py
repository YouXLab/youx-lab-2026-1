print('='*53)
print('BRINCANDO COM VOGAIS...')
print('='*53)
lista = ('hoje', 'azul', 'parte', 'coragem', 'computador', 'carro',
         'cachorro', 'jabuticaba', 'jericoacoara', 'filtro')
for p in range(0, len(lista)):
    for c in range(len(lista[p])):
        if c == 0:
            print(f'Na palavra \033[97m{lista[p].upper()}\033[m temos: ', end='')
        if lista[p][c] in 'aeiou':
            print(f'{lista[p][c]}', end=' ')
    print()