letra=str(input('digite uma frase :'))
print(f"quantas vezes a letra 'a' aparece na frase :{letra.count('a')} ")
print(f"a primeira letra apareceu na posicao :{letra.find('a')+1}")
print(f"em que posicao ela aparece pla ultima vez? :{letra.rfind('a')+1}")