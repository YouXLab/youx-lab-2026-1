n = int(input("Digite um número: "));
d = 0;
nu = "";
for i in range(1, n+1):
    if (n / i) % 1 == 0:
        d += 1;
        nu = nu + "{},".format(i);
if d > 2:
    print("O número {} foi dividido {} vezes pelos números: {} por tanto ele não é primo".format(n, d, nu));
elif d == 2:
    print("O número {} foi dividido apenas 2 vezes pelos números: {} por tanto ele é primo!".format(n, nu))