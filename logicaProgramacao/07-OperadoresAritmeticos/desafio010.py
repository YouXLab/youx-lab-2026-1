#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dolares ela pode comprar.
#considera US$ 1,00 = R$3,27

real = float(input('Quanto dinheiro voce tem na carteira? R$'))
dolar = real / 3.27
print('Com R${:.2f} voce pode comprar U${:.2f}'.format(real, dolar))