listagem = ('Palha de aço', 1.50,
            'Ypê',1.75,
            'Remédio',21.50,
            'Nutella',13.00,
            'Refrigerante',9.00,
            'Bolacha',3.80)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)