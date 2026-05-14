print('!@#$%¨&*()'*20)
print('Brincando com triângulos!!!')
print('!@#$%¨&*()'*20)
primeiro  = int(input('Primeiro segmento:'))
segundo = int(input('Segundo segmento:'))
terceiro = int(input('Terceiro segmento:'))

# Verifica se os dados formam um triângulo
if primeiro > segundo + terceiro or segundo > primeiro + terceiro or terceiro > primeiro + segundo:
    print('Não é possível formar um triângulo aqui sAbixão ')

# Triângulo equilátero
elif primeiro == segundo == terceiro:
    print("Triângulo equilátero")

# Triângulo escaleno
# elif primeiro != segundo != terceiro:
elif primeiro != segundo and primeiro != terceiro and segundo != terceiro:
    print("Triângulo escaleno!")

# Triângulo Isósceles
elif primeiro == segundo or primeiro == terceiro or segundo == terceiro:
    print("Triângulo Isósceles!")


