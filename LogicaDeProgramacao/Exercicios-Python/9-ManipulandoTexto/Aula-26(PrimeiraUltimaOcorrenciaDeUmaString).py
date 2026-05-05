nome = str(input('Digite uma frase: ')).upper()
print('A letra A aparece {} nesta frase'.format(nome.count('A')))
print('A primeira letra A aparece na posição {} desta frase'.format(nome.find('A')+1))
print('A ultima letra A aparece na posição {} desta frase'.format(nome.rfind('A')+1))

