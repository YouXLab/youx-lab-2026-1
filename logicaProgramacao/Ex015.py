Dias = int(input('Quantos dias alugados? '))
Km = float(input('Quantos Km rodados? '))
P = (Dias * 60) + (Km * 0.15)
print ('O valor do aluguel do carro foi R${:.2f}'.format(P))
