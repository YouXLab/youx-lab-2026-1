valorP = float(input('qual o valor do produto?'))
print('formas de pagamento ' 
      '[2] a vista cartao, ' 
      '[3] 2x no cartao, '
      '[4] 3x ou mais no cartao')
opcao= int(input('qual opcao ?'))
if opcao == 1:
    total = valorP - valorP * 10/100
    print(f'sua compra no dinheiro /cheque vai custar {total}')
elif opcao == 2:
     total = valorP - valorP * 5 /100
     print(f'sua compra com 5$ de desconto vai custar {total}')
elif opcao == 3:
    total = valorP
    parcela = total / 2
    print(f'a sua conta de {valorP} dividida em 2x no cartao vai custar {parcela}')
elif opcao == 4:
    total = valorP + valorP * 20/100
    print(f' sua conta de {valorP} dividido em 3x vai custar {total}')