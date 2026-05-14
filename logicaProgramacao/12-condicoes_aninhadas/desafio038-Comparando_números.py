numeroUm =int(input('primeiro número: '))
numeroDois =int(input('segundo número: '))
if numeroUm > numeroDois:
    print(f'o número {numeroUm} é maior que o {numeroDois}')
elif numeroDois > numeroUm:
    print(f'o número {numeroDois} é maior que {numeroUm}')
else:
    print('eles são iguais')