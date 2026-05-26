#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista_numero = []
maior = 0
menor = 0
opcao = ''
for numero in range(1, 5+1):
    num = int(input("Digite um valor: "))
    lista_numero.append(num)
    menor = num
    maior = num
    if num < menor:
        menor = num
    if num > maior:
        maior = num
print(lista_numero)
print(f"O menor numero é  {menor} e o maior é {maior}")
