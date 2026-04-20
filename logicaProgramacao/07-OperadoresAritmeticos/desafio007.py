#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostra a sua media.

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
media = (n1 + n2) / 2
print('A media entre {} e {} é igual a {}'.format(n1, n2, media))