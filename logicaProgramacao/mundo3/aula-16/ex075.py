lista = ''
primeiro = ''
pares = 0
for i in range(0,4):
    numero = int(input(f'digite o {i+1}° numero: '))
    if i == 0:
        primeiro = str(numero)
    if numero % 2 == 0:
        pares += 1
    lista += f'{int(numero)}'
    listaTupla = tuple(lista.split())
print(f'Voce digitou os valores {lista}')
print(f'O numero {primeiro} apareceu {lista.count(primeiro)} vezes')
if '3' in listaTupla:
    print(f'o numero tres apareceu na {lista.split().index("3")}')
else:
    print('o numero tres nao apareceu em nenhuma posicao. ')
print(f'ao todo foram  digitados {pares} numeros pares')