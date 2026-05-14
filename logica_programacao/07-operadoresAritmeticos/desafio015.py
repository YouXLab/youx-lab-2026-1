dia =int(input('Quantos dias ele ficou alugado?:'))

kilo =float(input(f'Quantos km você rodou durante o período de {dia} dias?:'))

pdia = dia * 60

pkilo = kilo * 0.15

print('                                          ')

print('||||||||||||||||||||||||||||||||||||||||')

print(f'O total a pagar é: R$ {pdia+pkilo}')

print('||||||||||||||||||||||||||||||||||||||||')