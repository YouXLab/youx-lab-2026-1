frase = str(input('Escreva uma frase: ').strip().lower().replace('',''))
f2 = (frase[::-1])
print(f2)
if frase == f2:
    print('Palíndromo')
else:
    print('Não é palíndromo')






