peso = float(input('Qual é o seu peso (KG):'))
altura = float(input('Qual a sua altura (M)'))
imc = peso / altura **2
print(f'O IMC(ÍNDICE DE MASSA CORPORAL) dessa pessoal é: {imc:.2f}')
if imc < 18.5:
    print('Mais leve que um palito de dente <3')
elif imc < 25:
    print('Seu normal aff veir juroooo')
elif imc < 30:
    print('Peso de um jumento...coincidência?')
elif imc < 40:
    print('Peso de caminhão')
elif imc > 40:
    print('Sua baleinha adultinha ;3 ')






