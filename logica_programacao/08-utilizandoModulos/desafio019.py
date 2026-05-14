import random
print('__________________________________________')

al1 =str(input('Nome do 1° estudante:'))
al2 =str(input('Nome do 2° estudante:'))
al3 =str(input('Nome do 3° estudante:'))
al4 =str(input('Nome do 4° estudante:'))
lista = [al1, al2, al3,al4]
escolhido=random.choice(lista)
print(f'O aluno escolhido foi: {escolhido}')

print('__________________________________________')
