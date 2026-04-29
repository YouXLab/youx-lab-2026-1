#Refaça o desafio009,mostrando a tabuada de um numero que o usuario escolher, so que agora utilizando um laço for.

num = int(input('Digite um numero pra ver a sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))   

