km = float(input('Quantos Km o carro percorreu? '))
d = float(input('Por quantos dias o carro foi alugado? '))
pg = (d * 60) + (km * 0.15)

print('O valor total a pagar é R${:.2f}'.format(pg))
