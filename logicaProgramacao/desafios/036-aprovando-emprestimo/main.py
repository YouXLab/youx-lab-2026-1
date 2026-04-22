v = int(input('Valor da casa: R$'));
s = int(input('Salário do comprador: '));
a = int(input('Quantos anos de financiamento? '));
p = v / (a * 12);
print('Para pagar uma casa de R${} em {} anos a prestação será de R${:.2f}'.format(v, a, p));
if p >= s * (30 / 100):
    print('Empréstimo NEGADO');
else:
    print('Empréstimo APROVADO');