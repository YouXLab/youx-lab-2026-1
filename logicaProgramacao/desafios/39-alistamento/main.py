from datetime import date;
a = date.today().year;
n = int(input("Em que ano você nasceu?: "));
i = a - n;
print("Quem nasceu em {} tem {} anos em {}".format(n, i, a));
if i < 18:
    print("Ainda faltam {} anos para o alistamento".format(18 - i))
    print("Seu alistamento será no ano {}".format(a + (18 - i)));
elif i > 18:
    print("Você já deveria ter se alistado há {} anos".format(a - (a - (i - 18))))
    print("Você se alistou em {}".format(a - (i - 18)));
elif i == 18:
    print("Você deve se alistar imediatamente!");