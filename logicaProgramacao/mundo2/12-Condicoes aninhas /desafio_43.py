peso = float(input('Qual e o seu peso (Kg) '))
altura = float(input('Qual e a sua altura?'))
imc = peso / (altura ** 2)
print('O ims dessa pessoa e de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce esta ABAIXO DO PESO normal')
elif 18.5 <= imc < 30:
    print('PARABENS,voce esta na faixa de PESO NORMAL')
elif 25 <= imc < 30:
        print('Voce esta em SOBREPESO')