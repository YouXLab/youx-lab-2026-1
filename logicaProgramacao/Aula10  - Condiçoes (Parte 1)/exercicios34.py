#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual é seu salário? '))

if salario <= 1250:
    print(f'Seu aumento será de R${(salario * 0.15):.2f} totalizando R${salario * 1.15:.2f}')
else:
    print(f'Seu aumento será de R${(salario * 0.10):.2f} totalizando R${salario * 1.10:.2f}')