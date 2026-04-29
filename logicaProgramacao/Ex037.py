Numero = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases para conversao')
print('[1] converter para binario')
print('[2] converter para octal')
print('[3] converter para hexadecimal')
opcao = input('Qual sua opcao: ')
if opcao == '1':
    print('{} convertido para binario e {}'.format(Numero,bin(Numero)[2:]))
elif opcao == '2':
    print('{} convertido para octal e {}'.format(Numero,oct(Numero)[2:]))
elif opcao == '3':
    print('{} ccnvertido para hexadecimal e {}'.format(Numero,hex(Numero)[2:]))
else:
    print('Opcao invalida, tente novamente')
