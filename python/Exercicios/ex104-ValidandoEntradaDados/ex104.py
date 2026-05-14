def leiaInt(num = ''):
    num = input('Digite um número: ')
    while num.isnumeric() is False:
        print('ERRO! Digite um número inteiro válido!')
        num = input('Digite um número: ')
    return int(num)


num = leiaInt('Digite um número')
print(f'Você acabou de digitar o número {num}')