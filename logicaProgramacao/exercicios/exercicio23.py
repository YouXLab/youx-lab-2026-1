numero  = int(input('informe um numero:'))
unidade = numero// 1 % 10
dezena  = numero// 10 % 10
cetena  = numero//100 % 10
milhar  = numero//1000 % 10
print('analisando o numero {}'.format(numero))
print("unidade:{}".format(unidade))
print('dezena:{}'.format(dezena))
print('cetena: {}'.format(cetena))
print('milhar:{}'.format(milhar))
