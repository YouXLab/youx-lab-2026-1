lista = [1,2,3,4,5,6,7]
for i in range(4, len(lista)):
    if lista[i] - 4 == lista[i-4]:
        print(lista[i], lista[i-4])