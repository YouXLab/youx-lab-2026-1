f = str(input('Digite uma frase: ')).upper().strip();
print('A letra A aparece na frase {} vezes'.format(f.count('A')));
print('A letra A aparece pela primeira vez na posição {}'.format(f.find('A')+1));
print('A letra A aparece pela primeira vez na posição {}'.format(f.rfind('A')+1));