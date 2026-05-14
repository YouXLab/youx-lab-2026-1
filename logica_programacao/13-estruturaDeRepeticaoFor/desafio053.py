print('------'*5)
print('BRINCANDO COM PALÍNDROMO E NÃO PALÍNDROMO....')
print('------'*5)
frase = input("Qual a frase? ").upper().replace(" ", "")
if frase == frase[::-1]:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")
print('FIM!!!')







