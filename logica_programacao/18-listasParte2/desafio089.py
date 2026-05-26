print('-='*53)
print(f'{"Avaliando alunos":^106}')
print('-='*53)
lista = [[], [[], [], []]]
escolha = contagem = mostrar = 0
while escolha != 'n':
    escolha = 0
    lista[0].append(input('Nome: '))
    numero1 = float(input('Nota 1: '))
    numero2 = float(input('Nota 2: '))
    lista[1][0].append(numero1)
    lista[1][1].append(numero2)
    lista[1][2].append((numero1 + numero2) / 2)
    while escolha != 'n' and escolha != 's':
        escolha = input('Quer continuar [S/N]? ').lower().strip()
print('-='*15)
print(f'Nº    NOME        {"MEDIA":>}')
print('=='*15)
for valor in lista[0]:
    print(f'{contagem}', end=' /')
    print(f'{valor:^11}', end=' /')
    print(f'{lista[1][2][contagem]:^13.1f}')
    contagem += 1
print('-='*15)
while mostrar != 999:
    mostrar = int(input('Mostrar notas de qual aluno? (999 para encerrar): '))
    if contagem > mostrar >= 0:
        print(f'As notas de {lista[0][mostrar]} são {lista[1][0][mostrar]} e {lista[1][1][mostrar]}')
        print('-='*15)
print('Programa encerrado :)')



