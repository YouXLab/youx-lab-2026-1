sexo = str(input('Informe seu sexo: [M/F] ').strip().upper())
while sexo not in "MmFf":
    str(input('Dados inválidos, informe seu sexo: '))
print('Sexo {} registrado!'.format(sexo))