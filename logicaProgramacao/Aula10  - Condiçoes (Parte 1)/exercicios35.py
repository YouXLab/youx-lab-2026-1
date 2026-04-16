#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('primeiro segmento: '))
b = float(input('segundo segmento: '))
c = float(input('terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
    print(f'os segmentos {a} , {b} e {c} podem formar um triangulo')
else:
    print(f'os segmentos {a} , {b} e {c} NAO podem formar um triangulo')