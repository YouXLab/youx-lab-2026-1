aluno = {}
a = []
aluno['Nome']=str(input('Nome: '))
aluno['Média']=float(input('Média: '))
a.append(aluno)
for c in a:
    for k, v in c.items():
        print(f'{k} é igual a {v}')
if aluno['Média'] >= 6:
    print('Situação é igual a aprovado')
if aluno['Média'] <= 5:
    print('Situação é igual a reprovado')