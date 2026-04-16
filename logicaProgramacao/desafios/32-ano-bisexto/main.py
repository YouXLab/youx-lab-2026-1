a = int(input("Digite o ano que deseja analisar: "));
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print("O ano {} é bisexto!".format(a));
else: 
    print("O ano {} não é bisexto".format(a));