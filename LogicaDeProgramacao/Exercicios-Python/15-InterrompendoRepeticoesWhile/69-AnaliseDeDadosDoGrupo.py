I = 0
M = 0
F = 0

while True:
    print('========================')
    print('  Cadastro de pessoas   ')
    Idade = int(input('Idade: '))
    Sexo = str(input('Sexo [M/F]: '))
    print('========================')
    N1 = str(input('  continuar? [S/N]: ').strip().upper())

    if Idade >= 18:
        I = I + 1
    if Sexo in 'Mm':
        M = M + 1
    if Sexo in 'Ff' and Idade >= 20:
        F = F + 1
    if N1 in 'Nn':
        break

print('========================')
print(f'Total de pessoas com 18 anos ou mais: {I}')
print(f'Total de homens: {M}')
print(f'Total de mulheres com 20 anos ou menos: {F}')