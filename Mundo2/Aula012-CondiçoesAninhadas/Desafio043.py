#Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostrea seu status, de acordo com a tabela abaixo:
#Abaixo de 18.5: Abaixo do Peso.
#Entre 18.5 e 25:Peso ideal.
#25 ate 30:Sobrepeso.
#30 ate 40:Obesidade.
#Acima de 40:Obesidade morbida.

peso = float(input('Qual é o seu peso? (Kg)'))
altura = float(input('Qual é a sua altura? (m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você esta ABAIXO do peso normal!')
elif 18.5 <= imc < 25:
    print('PARABENS,você está na faixa de PESO NORMAL!')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE, cuidado!')
elif imc >= 40:
    print('Você está em OBESIDADE MORBIDA, cuidado!')