pare = 0
ficha = []
opc = 0
while pare == 0:
    nome = str(input('Nome: '))
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2
    ficha.append([ nome, [nota_1 , nota_2] , media ])
    resposta = str(input('Quer continuar? [S/N]'))
    resp = resposta.upper()
    if resp == 'N':
        pare = 1
print('≃'*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('≃'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while opc == 0:
    escolha = int(input('Que mostrar qual aluno? (999 interrompe): '))
    if escolha == 999:
        opc += 1
    if escolha <= len(ficha) - 1:
        print(f'Notas de {ficha[escolha][0]} são {ficha[escolha][1]}')
print('THE END')