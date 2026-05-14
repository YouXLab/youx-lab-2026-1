peso =float(input('qual seu peso (Kg): '))
altura =float(input('qual sua altura (M): '))
imc = peso / altura ** 2
if imc < 18.5:
    print('abaixo do peso')
elif imc < 25:
    print('peso ideal')
elif imc < 30:
    print('sobrepeso')
elif imc < 40:
    print('obesidade')
elif imc > 40:
    print('obesidade morbida')
print(f'o imc da pessoa é: {imc:.2f}')



