dias =int(input('Quantos dias alugados? '))
Km =float(input('Quantos Km rodados? '))
pago = (dias * 60) + (Km * 0.15)
print('o total a pagar é R${:.2f}'.format(pago))