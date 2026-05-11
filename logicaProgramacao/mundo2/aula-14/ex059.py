numero1 = int(input("Primeiro Valor: "))
numero2 = int(input("Segundo Valor: "))
opcao = 0

while opcao != 5:
    print('''
          [1] somar
          [2] multiplicar
          [3] maior
          [4] novos números
          [5] sair do programa''')
    opcao = int(input("Escolha uma das opções: "))
    if opcao == 1:
        print(f"A soma dos dois números é: {numero1 + numero2}")
    if opcao == 2:
        print(f"A multiplicacao dos dois numeros e: {numero1 * numero2}")
    if opcao == 3:
        if numero1 > numero2:
            print(f"O {numero1} e maior que o {numero2}")
        if numero2 > numero1:
            print(f"o {numero2} e maior que o {numero1}")
    if opcao == 4:
        numero1 = int(input("Primeiro Valor: "))
        numero2 = int(input("Segundo Valor: "))