#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
numero = int(input("Digite um número para ver sua tabuada: "))
while numero >= 0:
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    numero = int(input("Digite outro número (negativo para sair): "))
print("Programa encerrado.")