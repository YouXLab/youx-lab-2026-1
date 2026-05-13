def leiaInt(inteiro):
    while True:
        try:
            int(inteiro)
        except:
            return False
        else:
            return True

def leiaFloat(real):
    while True:
        try:
            float(real)
        except:
            return False
        else:
            return True

inteiro = input('Digite um número inteiro: ')
while not leiaInt(inteiro):
    print('Erro: por favor digite um número inteiro válido.')
    inteiro = input('Digite um número inteiro: ')
real = input('Digite um número real: ')
while not leiaFloat(real):
    print('Erro: por favor digite um número real válido.')
    real = input('Digite um número real: ')
print(f'O valor inteiro digitado foi {inteiro} é o valor real digitado foi {real}.')