print('-='*20)
print('Analisador de Triângulo')
print('-='*20)
primeiro =float(input('Primeiro segmento: '))
segundo =float(input('Segundo segmento: '))
terceiro =float(input('Terceiro segmento: '))
if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < primeiro + segundo:
    print('os segmentos acima podem formar um triangulo')
else:
    print('os segmentos acima nao podem formar um triangulo')