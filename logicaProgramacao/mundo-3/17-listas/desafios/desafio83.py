expressao = str(input('Digite uma expressão: '))
lista = []
for caracteres in expressao:
    if caracteres == '(':
        lista.append(caracteres)
    elif caracteres == ')':
        if len(lista)>0:
            lista.pop()
        else:
            lista.append(')')
if len(lista) == 0:
    print('Sua expressão é valida.')
else:
    print('Sua expressão é invalida.')