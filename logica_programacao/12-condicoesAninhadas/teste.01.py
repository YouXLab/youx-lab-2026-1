# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
# condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros
v = float(input('Qual o valor da compra: R$'))
cores = {'clear': "\033[m",
         'red': '\033[31m',
         'green': '\033[32m',
         'yelow': '\033[33m',
         'blue': '\033[34m'}
print('=' * 50)
print(f'Método de pagamento:\n[{cores["red"]}1{cores["clear"]}] à vista dinheiro/cheque')
print(f'[{cores["green"]}2{cores["clear"]}] à vista no cartão')
print(f'[{cores["yelow"]}3{cores["clear"]}] 2x no cartão')
print(f'[{cores["blue"]}4{cores["clear"]}] 3x ou mais no cartão')
print('=' * 50)
num = int(input('Digite: '))
print('=' * 50)
if num == 1:
        desconto = (10/100)*v
        print(f'Sua compra será {cores["red"]} à vista dinheiro/cheque{cores["clear"]}.'
              f'\nCom um total de R${v:.2f}'
              f'\nO valor do desconto aplicado o total é de R${v-desconto:.2f}')
elif num == 2:
        desconto = (5 / 100) * v
        print(f'Sua compra será {cores["green"]} à vista no cartão{cores["clear"]}.'
              f'\nCom um total de R${v:.2f}'
              f'\nO valor do desconto aplicado o total é de R${v - desconto:.2f}')
elif num == 3:
        p = v/2
        print(f'Sua compra será {cores["yelow"]} 2x no cartão{cores["clear"]}.'
              f'\nO total de R${v:.2f} e cada parcela de R${p:.2f}')
elif num == 4:
        total_p = int(input('Quantas parcelas: '))
        print('=' * 50)
        juros = (20/100)*v
        p = v/total_p
        print(f'Sua compra será {cores["blue"]} 3x ou mais no cartão{cores["clear"]}.'
              f'\nCom o total de R${v+juros:.2f}'
              f' com o juros pelo parcelamento.'
              f'\nCom o total de parcelas igual a {total_p}x ao todo.\nMensalmente o valor pago é de R${p:.2f}')
else:
        print(f'{cores["red"]}ERRO!{cores["clear"]}')