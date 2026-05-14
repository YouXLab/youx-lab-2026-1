print('===============================================' * 2)
print('LOJA DE GUSTAVOS INDÚSTRIAS, VULGO A MELHOR E PIOR LOJA DO UNIVERSO ;)')
print('===============================================' * 2)
preco = float(input('Qual o valor da sua compra?:'))
print('FORMAS DE PAGAMENTO:\n[1]À VISTA/CHEQUE/PIX\n[2]À VISTA NO CARTÃO(DÉBITO)\n[3]2X NO CARTÃO (CRÉDITO)\n[4]3X OU MAIS NO CARTÃO (CRÉDITO)')
opcao = int(input('Qual a opção de pagamento: '))
if opcao == 1:
    total = preco - (preco * 0.1)
elif opcao == 2:
    total = preco - (preco * 0.05)
elif opcao ==3:
    total = preco
    parcela = total / 2
    print(f'Sua compra de 2X no cartão custará R${parcela} SEM JUROS!!!')
elif opcao == 4:
    total = preco + (preco * 0.2)
    totalDeParcelas = int(input('Quantas Parcelas?'))
    parcela = total / totalDeParcelas
    print(f'Sua compra de R${preco} dividida em {totalDeParcelas} parcelas custará R${parcela:.2f}')
print(f" Sua compra de R${preco} vai custar no final R${total}")






