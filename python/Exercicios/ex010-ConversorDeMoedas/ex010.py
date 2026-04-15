r = float(input('Quantos reais voce tem na carteira? R$'))
d = r / 3.27

print('Com R${:.2f}, você consegue comprar US${:.2f} '.format(r, d))