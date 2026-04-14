#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
ang = math.radians(float(input('Digite o angulo ')))
print(f' O seno é {math.sin(ang):.2f} , o cosseno é {math.cos(ang):.2f} e a tangente é {math.tan(ang):.2f}')
