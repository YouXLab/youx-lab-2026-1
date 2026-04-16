#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
n3 = int(input("Digite outro numero: "))
maior_numero = ''
menor_numero = ''
if n1 > n2 and n1 > n3:
 maior_numero = n1

if n2 > n1 and n2 > n3:
 maior_numero = n2
if n3 > n1 and n3 > n2:
 maior_numero = n3

#Verificando o menos valor

if n1 < n2 and n1 < n3:
 menor_numero = n1
if n2 < n1 and n2 < n3:
 menor_numero = n2
if n3 < n1 and n3 < n2:
 menor_numero = n3

print(f"O menor numero vai ser {menor_numero}")
print (f"O maior valor sera {maior_numero}")
