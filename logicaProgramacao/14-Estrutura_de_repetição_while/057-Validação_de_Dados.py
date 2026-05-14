sexo = 0
while sexo != 'M' and sexo != 'F':
    sexo = str(input('qual seu sexo: ')).upper()
    if sexo == 'M':
        print('masculino')
    elif sexo == 'F':
        print('feminino')
print('acabou')