Valor_Usuario = int(input('Digite um numero inteiro qualquer pra ver sua fatorial: '))
print(f"{Valor_Usuario}! = ", end='')
Numero = Valor_Usuario
fatorial = 1
while Numero != 0:
    print(f"{Numero}", end='')
    fatorial = fatorial * Numero

    if Numero != 1:
        print("x", end='')

    Numero = Numero - 1

print(f" = {fatorial}")
