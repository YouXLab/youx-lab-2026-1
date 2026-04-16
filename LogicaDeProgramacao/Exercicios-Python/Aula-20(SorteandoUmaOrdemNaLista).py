import random
N1 = str(input('Aluno-1 '))
N2 = str(input('Aluno-2 '))
N3 = str(input('Aluno-3 '))
N4 = str(input('Aluno-4 '))
Lista = [N1,N2,N3,N4]
random.shuffle(Lista)

print('A ordem será:')
print(Lista)
