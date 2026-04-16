v = float(input("Digite o valor da compra:"));
print("Selecione o método de pagamento:");
print("1 - A vista dinheiro/cheque");
print("2 - Á vista no cartão");
print("3 - Em até 2x no cartão");
print("4 - 3x ou mais no cartão");
o = int(input("Escolha a opção: "));
if o == 1:
    print("O valor de R$ {} fica por R$ {} pós o desconto de 10%".format(v, v - (v * (10 / 100))));
elif o == 2:
    print("O valor de R$ {} fica por R$ {} pós o desconto de 5%".format(v, v - (v * (5 / 100))));
elif o == 3:
    print("O total da compra ficou em R$ {}".format(v))
elif o == 4:
    print("O valor de R$ {} fica por R$ {} pós os juros de 20%".format(v, v + (v * (20 / 100))))