#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas geradas.
lista_par = []
lista_impar = []
lista = []
for numero in range (0,5):
    valor = int(input("Digite um numero: "))
    lista.append(valor)
    if valor % 2 == 0:
        lista_par.append(valor)
    else:
        lista_impar.append(valor)
print(f"A lista de numeros digitados é {lista}")
print(f"A lista de numeros pares é {lista_par}")
print(f"A lista de numeros em impares é {lista_impar}")
