def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro válido!')
            continue
        except (KeyboardInterrupt):
            print('\nEntrada de dados interrompida pelo usuário!')
            break
        else:
            return num

def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digite um número real válido!')
            continue
        except (KeyboardInterrupt):
            print('\nEntrada de dados interrompida pelo usuário!')
        else:
            return num


numint = leiaInt('Digite um número inteiro: ')
numfloat = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro {numint} e o número real {numfloat}.')