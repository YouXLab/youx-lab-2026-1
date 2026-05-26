def leiaInt(msg):
    ok = False
    valor = 0
    while not ok:
        numero = str(input(msg))
        if numero.isnumeric():
            valor = int(numero)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
    return valor

# Programa principal
numero = leiaInt('Digite um n: ')
print(f'Você acabou de digitar o número {numero}')
