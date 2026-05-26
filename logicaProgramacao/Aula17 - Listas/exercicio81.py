

lista_numerica = []
cont = 0
for numero in range(1, 5+1):
    valor = int(input("Digite um valor: "))
    if 5 in lista_numerica:
        print(f"{lista_numerica.count(5)}")
    lista_numerica.append(valor)
    cont += 1
print(f"{cont}")
lista_numerica.sort(reverse=True)
print (f"{lista_numerica.count(5)}")
print(lista_numerica)