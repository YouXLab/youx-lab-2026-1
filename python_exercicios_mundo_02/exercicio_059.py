#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa

#Seu programa deverá realizar a operação solicitada em cada caso.


numero1 = int(input("Primeiro valor: "))
numero2 = int(input("Segundo valor : "))
opcao = 0
while opcao != 5:
    print('''[ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = str(input("Escolha uma opção: "))
    if opcao == 1:
     soma = numero1 + numero2
     print(f"A soma de {numero1} e {numero2} é igual à {soma}")
    elif opcao == 2:
     multiplicacao = numero1 * numero2
     print(f"O resultado da multiplicação de {numero1} e {numero2} é igual à {multiplicacao}")
    elif opcao == 3:
     if numero1 > numero2:
        maior = numero1
     else:
        maior = numero2
     print(f"O maior numero é {maior}")
    elif opcao == 4:
     print("Informe os numeros: ")
     numero1 = int(input("Primeiro numero: "))
     numero2 = int(input("Segundo numero: "))
    elif opcao == 5:
     print("Finalizando")
    else:
     print("Opção Inválida")
print("Fim do programa")
