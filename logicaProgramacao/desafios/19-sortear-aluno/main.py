import random
a1 = input("Digite o nome do aluno 1:");
a2 = input("Digite o nome do aluno 2:");
a3 = input("Digite o nome do aluno 3:");
af = random.choice((a1, a2, a3))
print("{} foi o aluno sorteado aleatoriamente!".format(af))