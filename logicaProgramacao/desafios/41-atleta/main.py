from datetime import date
d = int(input("Digite seu ano de nascimento: "));
a = date.today().year;
i = a - d;
print("O atleta tem {} anos".format(i))
if i < 9:
    print("Sua categoria é Mirim.");
elif i < 14:
    print("Sua categoria é Infantil.");
elif i < 19:
    print("Sua categoria é Junior.");
elif i < 25:
    print("Sua categoria é Sênior.");
elif i > 25:
    print("Sua categoria é Master.")