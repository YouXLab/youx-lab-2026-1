import random

aluno1 = str(input('nome do Primeiro aluno: '))
aluno2 = str(input('nome do segundo aluno: '))
aluno3 = str(input('nome do terceiro aluno: '))
aluno4 = str(input('nome do quarto aluno: '))
chamada = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(chamada)
print('o aluno escolhido foi: {} '.format(escolhido))