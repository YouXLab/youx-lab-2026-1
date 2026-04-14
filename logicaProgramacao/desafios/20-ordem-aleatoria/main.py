import random
n1 = input("Digite o nome 1: ");
n2 = input("Digite o nome 2: ");
n3 = input("Digite o nome 3: ");
ordem = [n1, n2, n3];
al = random.shuffle(ordem);
print("A ordem de apresentação será: \n {}".format(ordem));