lista = []
mai = 0
men = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        mai = men = lista[c]
    else:
        if lista[c] > mai:
            mai = lista[c]
        if lista[c] < men:
            men = lista[c]
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {mai}')
print(f'O menor valor digitado foi {men}')