#Refaça o DESAFIO035 dos triangulos acrescentando o recurso de mostrar que tipo de triangulo sera formado:
#- Equilatero:Todos os lados iguais.
#- Isoceles:Dois lados iguais.
#-Escaleno:Todos os lados diferentes.

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmneto: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('O segmento acima PODEM FORMAR um triangulo ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 != r3:
        print('ESCALENO!')
    else:
        print('ISOCELES')
else:
    print('Os segmentos acima NAO PODEM FORMAR triangulo')