print('LOJAS AMERICANAS')
preco = float(input('Preco das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[1] a vista dinheiro ou cheque
[2] a vista no cartao
[3] 2x no cartao
[4] 3x olu mais no cartao''')
opcao = int(input('qual a opcao? '))
if opcao == 1:
    total = preco - (preco * 10 /100)
elif opcao == 2:
    total = preco - (preco * 5 /100)
print ('Sua compra de {:.2f} deu {} no final.'.format(preco, total))





