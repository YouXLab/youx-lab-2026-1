
n1 = int(input('digite o valor da compra'))
n2 = int(input('digite outro numero'))
opc = ''
while opc != 5:
    print('[1]somar'
          '[2]multiplicar'
          '[3]maior'
          '[4] novos numeros'
          '[5] sair do programa')
    opc=int(input('digite qual opcao'))
    if opc == 1:
        soma= n1+n2
        print( soma )
    elif opc == 2:
        multiplicar= n1*n2
        print(multiplicar)
    elif opc == 3:
        if n1 > n2:
            print(n1)
        else:
            print(n2)
    elif opc == 4:
        n1= int(input('digite um novo valor'))
        n2= int(input('digite um novo valor'))


