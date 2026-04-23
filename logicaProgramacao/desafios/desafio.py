n1 = 1
n2 = 2
n3 = 3
if n1 == n2 and n1 == n3 or n1 != n2 and n2 != n3:
    print("O jogo deu empate!")
elif n1 == n2 and n1 != n3:
    print("n3 ganhou")
elif n1 == n3 and n1 != n2:
    print("n2 ganhou")
elif n1 != n2 and n1 != n3:
    print("n1 ganhou")
