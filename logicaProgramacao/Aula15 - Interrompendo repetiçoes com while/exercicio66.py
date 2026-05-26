#Crie um programa que leia números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag)

cont = 0
soma = 0
num = 0
while num != 999:
    num = int(input("Digite um numero[ Digite 999 para parar ]: "))
    cont += 1
    soma += num
print(f"Voce digitou {cont-1} numeros e a soma entre eles é {soma-999}")