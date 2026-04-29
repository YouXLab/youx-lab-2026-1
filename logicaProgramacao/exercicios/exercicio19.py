import random
numero1 =str(input('primeiro aluno:'))
numero2 =str(input('segundo aluno:'))
numero3 =str(input('teceiro aluno:'))
numero4 =str(input('quarto aluno:'))
lista = [numero1,numero2,numero3,numero4]
escolhido = random.choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))