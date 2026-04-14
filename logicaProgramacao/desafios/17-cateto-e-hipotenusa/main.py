import math
c1 = float(input("Digite o cateto oposto: "));
c2 = float(input("Digite o cateto adjacente: "));
cs = math.sqrt(math.pow(c1,2) + math.pow(c2, 2));
print("A hipotenusa de {} e {} é: {:.2f}".format(c1,c2,cs))