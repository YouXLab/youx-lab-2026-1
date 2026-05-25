#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em
# uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores
# pares e ímpares em ordem crescente.


numero = [[],[]]
valor = 0
for c in range(1,8):
    valor = int(input("Digite um valor: "))
    if valor % 2 == 0:
         numero[0].append(valor)
    else:
         numero[1].append(valor)
numero[0].sort()
numero[1].sort()
print(f"os numeros pares digitados foram: {numero[0]}")
print(f"os numeros impares digitados foram: {numero[1]}")
