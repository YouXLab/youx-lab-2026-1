print('analisando triângulos')
primeiro =int(input('primeiro segmento: '))
segundo =int(input('segundo segmento: '))
terceiro =int(input('terceiro segmento: '))

if primeiro > segundo + terceiro or segundo > primeiro + terceiro or terceiro > primeiro + segundo:
    print('nao e possivel formar um triângulo')
elif primeiro == segundo == terceiro:
    print('triângulo equilatero')
elif primeiro != segundo and primeiro != terceiro and segundo != terceiro:
    print('triângulo escaleno')
elif primeiro == segundo or primeiro == terceiro or segundo == terceiro:
    print('triângulo isosceles')





