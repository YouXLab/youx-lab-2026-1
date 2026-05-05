
N1 = float(input('Digite o valor do pagamento: R$'))

print('Escolha uma dessas opções de pagamento.')
print('[1] à vista dinheiro/cheque: 10% de desconto')
print('[2] à vista no cartão: 5% de desconto')
print('[3] em até 2x no cartão: preço formal')
print('[4] 3x ou mais no cartão: 20% de juros')

N2 = (-N1 * 0.1) + N1
N3 = (-N1 * 0.05) + N1
N4 = N1 / 2
N6 = int(input('Sua escolha: '))

if N6 == 1:
    print(f'Você ira pagar R${N2} como o preço final.')
elif N6 == 2:
    print(f'Você ira pagar R${N3} como o preço final.')
elif N6 == 3:
    print(f'Você vai pagar 2 parcelas de R${N4}.')
elif N6 == 4:
    Parc = float(input('Quantas parcelas? '))
    N5 = ((N1 * 0.2) + N1) / Parc
    N7 = (N1 * 0.2) + N1
    print(f'Você ira pagar {Parc} parcelas de {N5} que o total vai ser {N7}.')
else:
    print('Este valor é invalido')