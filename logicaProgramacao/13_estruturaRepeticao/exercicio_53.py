frase= str(input('digite uma frase :')).strip().upper()
letra= frase.split()
junto= ''.join(letra)
inverso= ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('é polindromo')
else:
    print('nao é polindromo')
