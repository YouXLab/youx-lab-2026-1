palavra = input('digite uma palavra').replace(' ', '')
separado=palavra.split()
junto = ''.join(palavra)
inverso = ''
for palavras in range(len(junto) -1, -1, -1):
    inverso +=junto [palavras]
print(inverso)
if inverso == junto:
    print('é palindromo')
else:
    print('nao é palindromo')
