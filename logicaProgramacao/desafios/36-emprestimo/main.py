c = float(input("Digite o valor da casa: "));
s = float(input("Digite seu salario: "));
a = int(input("Digite anos de financiamento: "));
p = c / (a * 12);
print("Para pagar uma casa de R$ {} em {} anos a prestação será de R$ {:.2f}".format(c, a, p));
if p > s * (30 / 100):
    print("Financiamento negado!");
else: 
    print("Financimaneto aprovado!");