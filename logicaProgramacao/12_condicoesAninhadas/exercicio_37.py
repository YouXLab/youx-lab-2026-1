numero= int(input('digite um numero :'))
print('escolha uma das base para conversao: [ 1 ] converter para binario, [ 2 ] converter para octal, [ 3 ] converter para hexadecimal')
opcao= int(input('digite sua opcao'))
if opcao == 1:
    print(f'{numero} convertido para binario é igual {bin(numero)}')
if opcao == 2:
    print(f'{numero} convertido para octal é igual a {oct(numero)}')
if opcao == 3:
    print(f'{numero} convertido para hexadecimal é igual a {hex(numero)}')