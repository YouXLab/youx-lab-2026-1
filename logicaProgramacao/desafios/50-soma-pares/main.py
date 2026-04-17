n = 0;
co = 0;
for c in range(0, 6):
    i = int(input("Digite o número {}: ".format(c+1)));
    if i % 2 == 0:
        n += i;
        co += 1;
print("Você informou {} números pares, a soma deles deu {}".format(co, n))