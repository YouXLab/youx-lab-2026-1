frase = str(input('digite uma frase: ')).upper()
print(' A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('a primeira letra A apareceu na posiçao {}'.format(frase.find(A)+1))
print(' a ultima letra A apareceu na posiçao{}'.format(frase.rfind('A')+1))
