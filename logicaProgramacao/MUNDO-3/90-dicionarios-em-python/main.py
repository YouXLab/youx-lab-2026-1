aluno = dict()
aluno['nome'] = str(input('digite seu nome: '))
aluno['media'] = float(input(f'media de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'APROVADO'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'REPROVADO'
print(aluno)