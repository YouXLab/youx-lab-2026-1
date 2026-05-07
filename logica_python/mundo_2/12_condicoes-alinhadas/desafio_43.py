peso = float(input('qual seu peso? (km) '))
altura = float(input('qual seu altura? (m) '))
imc = peso / (altura ** 2)
print('o IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('voce esta ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('parabens voce esta na FAIXA DE  PESO NOMAL')
elif 25 <= imc < 30:
    print('voce esta em SOBREPESO')
elif 30 <= imc < 40:
    print('voce esa em OBESIDADE CUIDADO! ')
elif  imc >= 40:
    print('voce esta em OBESIDADE MOBIDA CUIDADO!')
    

