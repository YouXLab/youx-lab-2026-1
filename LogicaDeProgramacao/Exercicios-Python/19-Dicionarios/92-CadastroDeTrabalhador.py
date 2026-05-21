from datetime import date
pessoa = dict()
pessoa['Nome'] = str(input('Nome: '))
nasc = int(input(f'Ano de nascimento: '))
pessoa['Idade'] = date.today().year - nasc
trabalho = int(input('Carteira de trabalho [0 Não tem]: '))
if trabalho <= 0:
    pessoa['Ctps'] = 0
else:
    pessoa['Ctps'] = trabalho
    pessoa['Contratação'] = int(input(f'Ano de contratação: '))
    pessoa['Salario'] = float(input(f'Salario: '))
    pessoa['Aposentadoria'] = pessoa['Idade'] + ((pessoa['Contratação'] + 35) - date.today().year)
for a, b in pessoa.items():
    print(f'     - {a} é igual a {b}')

















