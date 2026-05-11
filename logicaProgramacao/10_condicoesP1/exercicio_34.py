salario= float(input('qual o seu salario? :'))
if salario <= 1.250:
    desconto= salario + (salario * 10/100)
else:
    desconto= salario + (salario * 15/100)
print(f'se voce ganhava {salario}, agora voce esta ganhando {desconto}')



