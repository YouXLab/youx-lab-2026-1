numero = int(input("Digite um numero para calcular seu fatorial: "))
calculo = numero
fatorial = 1
while calculo > 0:
    print(f"{calculo}", end= '')
    print(f" x " if calculo > 1 else ' = ', end= '')
    fatorial *= calculo
    calculo -= 1
print(f"{fatorial} ")