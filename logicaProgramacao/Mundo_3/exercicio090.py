#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#No final, mostre o conteúdo da estrutura na tela.




aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de aluno {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situaçao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situaçao'] = 'recuperaçao'
else:
    aluno['situaçao'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f'   -{k} é igual a {v}')