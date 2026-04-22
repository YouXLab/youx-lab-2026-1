p = int(input('Preço das compras: R$'));
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''');
o = int(input('Qual é a opção? '));
if o == 1:
    v = p - (p * 10/100);
elif o == 2:
    v = p - (p * 5/100);
elif o == 3:
    v = p;
    parcela = p /2;
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f}')
elif o == 4:
    v = p + (p *20/100);
    np = int(input('Quantas parcelas?'))
    parcela = v /np;
    print(f'Sua compra será parcelada em 3x de R${parcela:.2f}')
print(f'Sua compra de R${p:.2f} vai custar R${v:.2f} no final.')