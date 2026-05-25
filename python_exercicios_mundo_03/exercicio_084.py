#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:

#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.


pessoas = []
dados = []
menor = []
continuar = "S"
while continuar == "S":
    dados.append(input("Nome: "))
    dados.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        maior = dados[1]
        menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    continuar = input("Quer continuar? [S/N] ").upper()
print(f"Cadastraram {len(pessoas)} pessoas")
print(f"O maior peso foi {maior}kg", end = " ")
for peso in pessoas:
    if peso[1] == maior:
        print(f"[{peso[0]}]", end = " ")
print()
print(f"O menor peso foi {menor}kg", end = " ")
for peso in pessoas:
    if peso in pessoas[1] == menor:
        print(f"[{peso[0]}]", end = " ")
