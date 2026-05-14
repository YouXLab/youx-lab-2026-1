preco =int(input('qual o valor da sua compra?: '))
print('formas de pagamento:\n[1] À vista/cheque/pix\n[2] a vista no cartao(debito)\n[3]2x no cartao(credito)\n[4]3x ou mais no cartao(credito)')
opcao =int(input('qual a opção de pagamento: '))
if opcao == 1:
    total = preco - (preco * 0.1 )
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'sua compra de {preco} dividida em duas vezes no cartao de credito custará {parcela} sem juros')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalDeparcelas =int(input('quantas vazes voce quer parcelar: '))
    parcela = total / totalDeparcelas
    print(f'sua compra de {preco} divifidida em {totalDeparcelas} parcelas com juros passara a custar {parcela}')

print(f'Sua compra de {preco} custará no fim {total}')