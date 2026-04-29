Produto = float(input('Qual o valor do produto: '))
print('Escolha um metodo de pagamento:')
print('[1]-A Vista em Dinheiro/Cheque (10% de desconto)')
print('[2]-A Vista no cartao (5% de desconto)')
print('[3]-Em ate 2x no cartao (Preco normal)')
print('[4]-3x ou mais no cartao (20% de juros)')
opcao = int(input('Qual a opcao: '))
if opcao == 1:
   Produto2 = Produto - Produto * (10 / 100)
   print('O produto vai custar R${:.2f}'.format(Produto2))
elif opcao == 2:
    Produto3 = Produto - Produto * (5 / 100)
    print('O produto vai custar R${:.2f}'.format(Produto3))
elif opcao == 3:
    print('O produto vai custar R${:.2f}'.format(Produto))
elif opcao == 4:
    Produto4 = Produto * 1 + Produto * (20 / 100)
    Parcelas = int(input('Quantas parcelas? '))
    Parcelas2 = Produto4 / Parcelas
    print('As parcelas vao ser de {}x de {:.2f}R$ com JUROS'.format(Parcelas, Parcelas2))
    print('O produto vai custar {:.2f}R$'.format(Produto4))
else:
    print('Opcao invalida, tente novamente')