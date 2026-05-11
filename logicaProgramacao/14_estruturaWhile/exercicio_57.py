sexo= str(input('digite seu sexo')).strip().upper()
while sexo not in 'MmFf':
    sexo= str(input('informe novamente')).strip().upper()
print('obrigado por registrar aqui !')