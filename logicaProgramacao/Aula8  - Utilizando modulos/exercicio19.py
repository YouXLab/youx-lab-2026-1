#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice
n1 = input("Digite o nome do aluno ")
n2 = input("Digite o nome do aluno ")
n3 = input("Digite o nome do aluno ")
lista = [n1 , n2 , n3]
resultado = choice(lista)
print (f"O aluno escolhido foi o {resultado}")