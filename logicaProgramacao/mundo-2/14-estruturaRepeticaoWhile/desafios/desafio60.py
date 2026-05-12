numero = int(input('Digite um numero: '))
antecessor = numero - 1
resultado = 0
while antecessor > 0:
    if resultado == 0:
        fatorial = numero * antecessor
        resultado = fatorial
        antecessor -= 1
    else:
        fatorial = resultado * antecessor
        resultado = fatorial
        antecessor -= 1
print(resultado)