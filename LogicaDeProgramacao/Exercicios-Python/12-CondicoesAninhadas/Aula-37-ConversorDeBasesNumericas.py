N1 = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases para conversão: ')
print('[1] BINARIO')
print('[2] OCTAL')
print('[3] HEXADECIMAL')
N2 = int(input(''))
if N2 == 1:
    print('O numero {} em BINARIO é: {}'.format(N1, bin(N1) [2:]))

elif N2 == 2:
    print('O numero {} em OCTAL é: {}'.format(N1, oct(N1)[2:]))

elif N2 == 3:
    print('O numero {} em HEXADECIMAL é: {}'.format(N1, hex(N1)[2:]))

else:
    print('Escolha um dos 3 numeros')