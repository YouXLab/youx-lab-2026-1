def leiaInt(numero):
    teste = 0
    while teste != 1:
        if numero.isnumeric():
            teste = 1
        else:
            print("ERRO!", end=' ')
            numero = input("Digite um número válido: ")
    return numero

num = leiaInt(input("Digite um número: "))
print(f'Você acabou de digitar o número {num}')