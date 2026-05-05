ano = int(input('Que ano quer ver? '))
if ano % 4 and ano % 100 != 0 or ano % 400 == 0:
    print('Este ano não é bissexto')
else: print('Este ano é bissexto')