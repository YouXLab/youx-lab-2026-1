N1 = 0
N2 = 0
N3 = 0
ST = 999999999999999
nome1 = ' '


print('=====================================')
print('Lojas Compre UM Pague DOIS ')
while True:
    print('=====================================')
    Nome = input('Nome do produto: ')
    P1 = float(input('Preço do produto: '))
    SN = str(input('Quer continuar as compras? [S/N]: ').strip().upper())
    N1 = N1 + P1
    if P1 >= 1000:
        N2 = N2 + 1
    if P1 <= ST:
        ST = P1
        nome1 = Nome
    if SN in 'Nn':
        break
print('=====================================')
print(f'O total das compras foi: R${N1}.')
print(f'Temos {N2} produtos mais caros que R$1000.')
print(f'O produto mais barato foi {nome1} e custou R${ST}.')
print('=====================================')

