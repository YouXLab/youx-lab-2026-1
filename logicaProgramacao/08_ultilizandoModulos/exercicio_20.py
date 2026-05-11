import random
aluno1=str(input('o nome desse aluno é'))
aluno2=str(input('esse chama'))
aluno3=str(input('esse chama'))
aluno4=str(input('esse chama'))
lista=[aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print(lista)
