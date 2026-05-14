sexo = ''
while sexo != 'M' or sexo != 'F':
 sexo= str(input('informe seu sexo: [M/F] ')).upper()
 if sexo == 'M' or sexo == 'F':
  print(f'sexo {sexo} registrado')
 else:
  print('sexo invalido,tente outra vez')