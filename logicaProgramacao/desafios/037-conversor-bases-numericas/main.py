n = int(input('Digite um número inteiro: '));
print('''Escolha uma das bases para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para COCTAL
[ 3 ] converter para HEXADECIMAL''');
o = int(input('Sua opção: '));
if o == 1:
    print('{} para BINÁRIO é igual a {}'.format(n, bin(n)));
elif o == 2:
    print('{} para COCTAL é igual a {}'.format(n, oct(n)));
elif o == 3:
    print('{} para HEXADECIMAL é igual a {}'.format(n, hex(n)));
else:
    print('Escolha uma das opções: ');