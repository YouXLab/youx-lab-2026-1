F1 = str(input('Digite uma frase: ')).upper()
F2 = F1.split()
F3 = ' '.join(F2)
F4 = F3[::-1]

print(f'O inverso de {F3} é {F4}')
if F3 == F4:
    print('É palindromo')
else:
    print('Não é palindromo')