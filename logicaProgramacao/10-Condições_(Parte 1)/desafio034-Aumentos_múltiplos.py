salario =int(input('qual é o salario do funcionario?: '))
if salario <=1250:
    novoSalario = ((salario * 15 / 100) + salario)
else:
    novoSalario = ((salario * 10 / 100) + salario)
print(f'quem ganhava {salario} passou a receber {novoSalario}')
