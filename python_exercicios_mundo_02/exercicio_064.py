#Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).


numero = 0
conta = 0
soma = 0
while numero != 999:
    numero = int(input("Digite um número: "))
    soma += numero
    conta += 1
print(f"Voce digitou {conta} números e a soma entre eles é {soma}")

