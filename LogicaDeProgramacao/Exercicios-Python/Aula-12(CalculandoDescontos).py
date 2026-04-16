N1 = float(input('Qual o preço do produto? R$'))

N2 = N1 - (N1 * 5 / 100)

print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(N1, N2))