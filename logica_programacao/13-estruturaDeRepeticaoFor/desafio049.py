print('-----------------------------------------------')
tabuada =int(input('Me diga um número para mostrar a tabuada dele:'))
for numero in range(0, 11):
    for contagem in range(0, 11):
        print(f'{contagem} * {numero} = {contagem * numero}')
print('-----------------------------------------------')