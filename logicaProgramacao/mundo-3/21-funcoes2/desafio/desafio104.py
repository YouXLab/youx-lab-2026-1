def leiaInt(numero):
    while not numero.isnumeric():
        if numero.isnumeric() == True:
            return
        else:
            numero = input('ERRO! Digite um número interio válido: ')

    return numero

numero = leiaInt(input('Digite um número: '))
print(f'Você digitou o número {numero}')