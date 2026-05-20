sexo = str(input('informe seu sexo: [M/F)')).strip().upper()[0]
while sexo not in 'Mf':
    sexo = str(input('Dados invalidos, Por Favor, informe seu sexo:')).strip().upper()[0]
    print('Sexo {} registrado com sucesso'.format(sexo))