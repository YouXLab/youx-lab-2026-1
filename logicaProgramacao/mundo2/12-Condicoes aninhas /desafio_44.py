print('{:=^40}' .format('LOJA DA ACSA'))
preco = float(input('O preco das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] a vista dinheiro/cheque 
[ 2 ] a vista cartao
[ 3 ] 2x no cartao 
[ 4 ] 3x ou mais  no cartao''')
opcao = int(input('Qual e a opcao?'))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
print('Sua compra de {.:2f} vai custar R${} no final'.format( preco,total))