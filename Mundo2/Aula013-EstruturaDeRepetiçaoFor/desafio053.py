#Crie um programa que leia uma frase qualquer e diga se ela é um polindromo,desconsiderando espaços:

f = str(input('Digite uma frase: '))
e = "".join(f.split()).lower()
if e == e[::-1]:
    print('E um polindromo')
else:
    print('Nao é um polindromo')