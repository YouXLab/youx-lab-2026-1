a = float(input('Digite o valor da primeira reta'))
b= float(input('Digite o valor da segunda reta'))
c = float(input('Digite o valor da terceira reta'))

if (a < b + c) and (b < a + c) and (c < a + b):
    print('Essas retas podem formar um triângulo!')
else:
    print('As restas não podem formar um triângulo!')