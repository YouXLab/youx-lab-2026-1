
print('========= LOJA DA ANA =======')
preco =float(input('digite o valor do produtos: '))
print('FORMAS DE PAGAMENTOS')
print('[1] - Á vista no dinheiro ')
print('[2] - Á vista no cartão ')
print('[3] - Em ate 2x no cartão ')
print('[4] - 3x ou mais no cartão ')
opcao =int(input('qual é a opção de pagamento?'))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100 )
    print(f'sua compra de R${preco} vai custar R${total} no final')
elif opcao == 3:
    total = preco
    parcela = total /2
    print(f'sua compra sera parcelada em 2x deR${parcela}  SEM JUROS')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    total_da_parcelas =int(input('quantas parcelas?'))
    parcela = total / total_da_parcelas
    print(f'sua compra sera parcelada em {total_da_parcelas}x  de R${parcela} COM JUROS!')
    print('sua compra  de  R${:.2f} vai custar R${:.2f} no final'.format(preco,total))





