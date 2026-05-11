#crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#no final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

numero = 0
cont = 0
soma = 0
while numero != 999:
    numero = int(input('Digite seu numero [para parar digite 999]: '))
    if numero != 999:
        cont += 1
        soma += numero
print(f'voce digitou {cont} numeros e a soma deles foi {soma}')