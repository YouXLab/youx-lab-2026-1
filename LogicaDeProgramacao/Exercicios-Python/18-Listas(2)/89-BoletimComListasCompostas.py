ficha = list()
nome = str(input('Nome: '))
nota1 = int(input('Nota [1]: '))
nota2 =  int(input('Nota [2]: '))
SN = str(input('Deseja continuar? [S/N] ').strip().upper())
media = (nota1 + nota2) / 2
ficha.append([nome, [nota1, nota2], media])
while SN not in 'Nn':
    nome = str(input('Nome: '))
    nota1 = int(input('Nota [1]: '))
    nota2 =  int(input('Nota [2]: '))
    SN = str(input('Deseja continuar? [S/N] ').strip().upper())
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
print('-='*15)
print(f'{'No.':<4}{'Nome.':<10}{'Media.':>8}')
print('--'*15)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
N = int(input('Deseja ver a nota de qual aluno? [-1 interrompe]: '))
while N != -1:
    for i, a in enumerate(ficha):
        if i == N:
            print(f'Notas de {a[0]} são: {a[1]}')
    N = int(input('Deseja ver a nota de qual aluno? [-1 interrompe]: '))