lista = ('programacao', 'computador', 'codigo', 'python', 'aprender', 'estudar', 'futuro', 'trabalhar')
for palavra in lista:
    print(f'\nNa palavra {palavra} temos', end=' ')
    for vogais in palavra:
        if vogais.lower() in 'aeiou':
            print(vogais, end=' ')

