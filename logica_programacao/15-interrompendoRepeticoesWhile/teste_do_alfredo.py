quantidade_de_opcoes = 0
contador = 0

while True:
    print('[1]PÉSSIMO\n[2]RUIM\n[3]OK\n[4]BOM\n[5]EXELENTE')
    print('[Q] PARA SAIR/ENCERRAR O PROGRAMA.')
    escolha = str(input('ESCOLHA UMA OPÇÃO:')).upper().strip()

    if escolha == "Q":
        break

    if escolha =='1' or escolha =='2' or escolha =='3' or escolha == '4' or escolha == '5':
        escolha_de_numero = int(escolha)
        print('aaaaaa')
        contador = contador + 1
    else:
        print("valor invalido")

print(f"{contador} escolhas feitas")