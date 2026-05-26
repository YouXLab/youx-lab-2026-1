exp = str(input('Digite uma expressão: '))
cont = exp.count('(')
cont_2 = exp.count(')')
if (cont + cont_2) % 2 == 0 :
    print('A expressão é  valida.')
else:
    print('A expressão não é valida.')
