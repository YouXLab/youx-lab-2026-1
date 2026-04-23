import random
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno:'))
aluno3 = str(input('Digite o nome do primeiro aluno: '))
aluno4 = str(input('Digite o nome do segundo aluno: '))
lista_alunos = [aluno1 ,aluno2, aluno3, aluno4]
sorteado = random.choice(lista_alunos)
print('O sorteado foi {}'.format(sorteado))
