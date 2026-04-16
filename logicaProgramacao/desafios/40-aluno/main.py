n1 = float(input("Digite a primeira nota: "));
n2 = float(input("Digite a segunda nota: "));
m = (n1 + n2) / 2
if m < 5:
    print("REPROVADO!");
elif m < 6.9:
    print("Em recuperação.");
elif m > 7:
    print("Aprovado!");