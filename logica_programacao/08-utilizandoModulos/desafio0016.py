import math
#importei a 'biblioteca' math

num = float(input('Digite um valor:'))
#criei a variavel 'num' e a proposta: digite um valor

print(f'O valor Digitado foi: {num} e a sua Porção inteira vale {math.trunc(num)}')
#por fim criei a 'resposta' da maquina...usando 'f' antes de aspas para indicar q é format ao inves de usar .format| apos isso indiquei num no primeiro chaves e depois usei math.trunc(num) no outro chaves! <- trunc de num para eliminar todos os numeros depois da virgula E DEU CERTO ;)
