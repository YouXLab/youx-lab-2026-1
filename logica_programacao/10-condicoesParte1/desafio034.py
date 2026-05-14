salario = float(input('Qual o salário do seu funcionário?:'))
if salario <=1250:
    novoSalario = ((salario * 15 / 100) + salario)
else:
    novoSalario = ((salario * 10 / 100) + salario)
print(f'De acordo com o seu salário R${salario},00 você recebeu um aumento... \nPortanto seu novo salário é: R${novoSalario}')


