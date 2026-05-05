N1 = float(input('Escreva a nota do primeiro aluno: '))
N2 = float(input('Escreva a nota do segundo aluno: '))
N3 = (N1 + N2) / 2

if N3 < 6:
    print('Reprovado')
elif N3 > 6:
    print('Passou no teste')
else:
    print('ERRO')