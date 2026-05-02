ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = ((nota1+nota2)/2)
    ficha.append([nome, [nota1, nota2], media])
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break
print('-='*12)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*24)
for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    print('-' * 24)
    opcao = int(input('Mostrar notas de qual aluno? (999 para finalizar): '))
    if opcao == 999:
        break
    if opcao <= len(ficha)-1:
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')
print('Volte sempre!')