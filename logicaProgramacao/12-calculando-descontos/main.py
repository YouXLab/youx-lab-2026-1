preço = float(input('qual e o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('o produto que custava R${: .2f}, na promoçao com desconto de 5% vai custar R${: .2f}'.format(preço, novo))
