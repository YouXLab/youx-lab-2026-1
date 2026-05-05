peso = float(input('qual o seu peso?'))
altura = float(input('qual sua altura?'))
imc= peso/(altura * altura )
print(f'o IMC dessa pessoa é {imc}')
if imc < 18.5:
    print('abaixo do peso')
elif imc >=18.5:
    print('peso ideal')
elif imc >= 25:
    print('sobrepeso')
elif imc >= 30:
    print('obesidade')
elif imc > 40:
    print('obesidade morbida')
