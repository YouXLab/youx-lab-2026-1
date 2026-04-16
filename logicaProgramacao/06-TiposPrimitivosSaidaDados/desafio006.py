#Desafio003 aula 006:
#Crie um programa que leia dois numeros e mostra a soma entre eles.

n1 = int(input('digite um numero'))
n2 = int(input('digite mais um numero'))
s = n1 + n2
print('a soma vale',s)

#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informaçoes possiveis sibre ela.
n = float(input('Digite um valor: '))
print(n)

#Verdadeiro e falso se e um numero numerico.
n = bool(input('Digite um valor: '))
print(n)

#Se é letra:
n = input('Digite algo: ')
print(n.isalpha())
