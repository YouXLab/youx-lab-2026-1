viagem = float(input('Qual é a distância da viagem? '))

if viagem <= 200:
    valor = viagem * 0.50
    print('O valor da passagem será de R${:.2f}'.format(valor))
else:
    valor = viagem * 0.45
    print('O valor da passagem será de R${:.2f}'.format(valor))
