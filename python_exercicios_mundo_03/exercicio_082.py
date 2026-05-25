#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.


lista = []
pares = []
impares = []
resposta = "S"
while resposta == "S":
    numero = int(input("Digite um numero: "))
    lista.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
        resposta = input("Quer continuar? [S/N] ").upper()
print(f"Lista completa: {lista}")
print(f"Numeros pares: {pares}")
print(f"Numeros impares: {impares}")
