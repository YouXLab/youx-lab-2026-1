def leiaInt(frase):
    numero = input(frase)
    while not numero.isdecimal():
        print('\033[31mERRO! Digite um número inteiro.\033[m')
        numero = input(frase)
    numero = int(numero)
    return numero



n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')