produto=float(input('qul o valor do produto'))
print('formas de pagamento '
      '[1] a vista dinheir/cheque,'
' [2] a vista cartao, '
'[3] 2x no cartao,'
' [4] 3x ou mais no cartao')
opcao= int(input('qual a opcao? :'))
if opcao == 1:
    total = produto - produto * 10/ 100
    print(f'sua compra no dinheiro/cheque vai custar {total}')
elif opcao == 2:
    total = produto - produto * 5 / 100
    print(f'sua compra com 5$ de desconto vai custar {total}')
elif opcao == 3:
    total = produto
    parcela = total / 2
    print(f'sua conta de {produto} divida em 2x no cartao, vai custar {parcela}')
elif opcao == 4:
    total = produto + produto * 20/ 100
    print(f'sua conta de {produto} dividido em 3x vai custar {total}')


