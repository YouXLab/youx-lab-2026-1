valor1= float(input('digte um valor : '))
valor2= float(input('digte outro valor : '))
opcao = 0

while opcao != 5:

    if opcao == 1:
        soma = valor1 + valor2
        print(f"A soma de {valor1} com {valor2} é: {soma}")
    if opcao == 2:
        multiplicar= valor1 * valor2
        print(f'a multiplicação de {valor1} com {valor2} é de {multiplicar}' )
    if opcao == 3:
        maior= valor1 > valor2
        print(f'se {valor1} for maior que {valor2} o resultado será de {maior}')
    if opcao == 4:
        novo= int(input('quais novos numeros voce quer adicionar?'))
        print(f'voce adicionou {novo} como um novo numero.')
    if opcao == 5:
        print('saindo do programa')

    print('''
        [1]somar
        [2]multiplicar
        [3]maior
        [4]novos numeros
        [5]sair do programa
        ''')
    opcao = int(input('qual opcao voce deseja? : '))
