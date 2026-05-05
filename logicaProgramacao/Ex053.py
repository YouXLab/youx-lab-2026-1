Frase = input('Digite uma frase: ').lower()
Frase2 = Frase.replace(" ","")
Frase3 = Frase2[::-1]
print(f'O Inverso da frase {Frase} e {Frase3}')
if Frase2 == Frase3:
    print('A frase e palindromo')
else:
    print('A frase nao e palindromo')
