boletim = []
aluno = []
resposta = 'S'
while resposta == 'S':
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    aluno.append(media)
    boletim.append(aluno[:])
    aluno.clear()
    resposta = str(input('Quer continuar? [S/N] ')).upper()
    while resposta not in 'SN':
        print('Resposta inavalida. Tente novamente')
        resposta = str(input('Quer continuar? [S/N] ')).upper()
print(f'{'No.':<5} {'Aluno':<10} {'Media'}')
for a in range(0, len(boletim)):
    print(f'{a:<5} {boletim[a][0]:<10} {boletim[a][3]}')
mostrar = int(input('Mostrar nota de qual aluno? (999 para parar) '))
if mostrar != 999:
    print(f'As notas de {boletim[mostrar][0]} são {boletim[mostrar][1:3]}')
