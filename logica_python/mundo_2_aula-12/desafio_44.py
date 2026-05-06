
print('{:=^40}'.format(' LOJAS ALLANAS'))
preco = float(input('preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
 [1] à vista dinheiro/cache
 [2] à vista cartao
 [3] 2x no cartao
 [4] 3x ou mais no cartao''')
opcao = int(input('qual é a opsao? '))
if opcao == 1:
    valor_total = preco * 0.9
elif opcao == 2:
    valor_total = preco * 0.95
elif opcao == 3:
    valor_total = preco
elif opcao == 4:
    valor_total = preco * 1.2
else:
    valor_total = None
    print('opcao INVALIDA ')

if valor_total != None:   # isso é igual a --> if Valor_total
    print(f"o preço total é {valor_total}")
