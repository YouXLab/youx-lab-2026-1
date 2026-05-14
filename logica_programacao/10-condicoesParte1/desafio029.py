from traceback import print_tb

velocidade =int(input('Qual a velocidade atual do seu carro?:'))
valorDaMulta = ((80 - velocidade) * -1) * 7
if velocidade >=80:
    print('Multado!!! você ultrapassou a velocidade permitida que é 80km/h')
else: velocidade <80
print(f'Tenha um excelente dia e dirrija com segurança!!! você deve pagar R$ {valorDaMulta},00 de multa!')
