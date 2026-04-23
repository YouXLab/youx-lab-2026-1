sexo = str(input('Informe seu sexo [M/F]: ')).strip()[0]
while True:
    if sexo not in 'MmFf':
        print('DADOS INVÁLIDOS!')
        sexo = str(input('Informe seu sexo [M/F]: ')).strip()[0]
    else:
        break
