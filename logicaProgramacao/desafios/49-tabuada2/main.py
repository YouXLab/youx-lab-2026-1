n = int(input("Digite um número para ver sua tabuada: "));
for c in range(0, 10):
    print("{} x {} = {}".format(n, c+1, n * c+1))