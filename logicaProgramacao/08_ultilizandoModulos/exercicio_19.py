import random
aluno1= str(input('nome do aluno 1: '))
aluno2= str(input('nome do aluno 2: '))
aluno3= str(input('nome do aluno 3: '))
aluno4= str(input(' nome do aluno 4: '))
lista= [aluno1, aluno2, aluno3, aluno4]
sorteio= random.choice(lista)
print(f'o aluno sorteado foi o {sorteio}')