import ntpath
from email.header import BSPACE

algo =input('Me diga qualquer coisa:')

print('Coisa respondida:',algo)

print('Seu tipo Primitivo é:',type(algo))

print('Só tem espaços:',algo.isspace())

print('É um número:',algo.isnumeric())

print('É alfabético:',algo.isalpha())

print('É alfanúmerico:',algo.isalnum())

print('Está em TUDO Maiúsculo',algo.isupper())

print('Alguma letra está em minúsculo:',algo.islower())

print('Capitalizado:',algo.capitalize())