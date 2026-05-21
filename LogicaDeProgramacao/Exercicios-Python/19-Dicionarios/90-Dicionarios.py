aluno = dict()
aluno['Nome'] = str(input('Nome do aluno: '))
aluno['Media'] = float(input(f'Media de {aluno['Nome']}: '))

if aluno['Media'] >10:
    aluno['Situação'] = 'Aprovado'
elif aluno['Media'] <10 and aluno['Media'] >5:
    aluno['Situação'] = 'Reculperação'
elif aluno['Media'] <5:
    aluno['Situação'] = 'Reprovado'
print('--'*20)
for a, b in aluno.items():
    print(f'     -{a} é igual a {b}')
















