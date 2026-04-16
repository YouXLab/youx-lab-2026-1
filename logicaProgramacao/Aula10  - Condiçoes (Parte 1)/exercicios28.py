from random import choice
lista = [1 , 2 , 3 , 4 , 5]
resultado = choice(lista)
n2 = int(input(f"Qual numero eu estou pensando?  "))
if n2 == resultado:
 print("Voce acertou")
else:
 print(f"VOce errou, eu estava pensando no numero {resultado}")
if n2 >= 6:
 print("Escolha um numero de 0 a 5!!")



