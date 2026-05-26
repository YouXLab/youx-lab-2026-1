
saldo = 0
opc = ''
print("BEM VINDO")
while opc !=4:
    print("[1] VER SALDO \n [2] DEPOSITAR \n [3] SACAR \n [4] EXIT")
    opc = int(input(""))
    if opc ==1:
        print(f"O saldo atual da conta é de R${saldo:.2f}")
    elif opc ==2:
        deposito = float(input("Digite o valor que será depositado: R$"))
        if deposito <0:
            print("Coloque uma quantia real")
        else:
            saldo += deposito
    elif opc ==3:
        sacar = float(input("Digite o valor voce irá sacar: R$"))
        if sacar <0:
            print("")
        if sacar >= saldo:
            print("Voce nao possui essa quantia para saque")
        else:
            saldo -= sacar
    else:
        print("Escolha uma das opcoes disponiveis abaixo")
print("Volte sempre")





