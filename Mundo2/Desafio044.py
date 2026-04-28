#Elabora um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condiçao de pagamento:
# -a vista dinheiro/cheque: 10% de desconto.
# -a vista no cartao: 5% de desconto.
# -em ate 2x no cartao:preço normal.
# -3x ou mais no cartao: 20% de juros.

print('{:=^40}'.format(' LOJAS ANA VALERIO '))
preco = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[1] á vista dinheiro/cheque
[2] á vista cartao
[3] 2x no cartão 
[4] 3x ou mais no cartao''')
opcao = int(input('Qual é a opçao? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
    print(f"O total é R${total}")

elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print('Sua compra de {:.2f} vai custar R${:.2f} no final.'.format(preco, total))