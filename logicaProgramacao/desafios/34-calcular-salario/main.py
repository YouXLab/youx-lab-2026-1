s = float(input("Digite o valor do salario: "));
a = 0;
if s >= 1250:
    a = 10;
else: 
    a = 15;
print("Quem ganhava R$ {} passa a ganhar R$ {} agora".format(s, s + s * (a / 100)))