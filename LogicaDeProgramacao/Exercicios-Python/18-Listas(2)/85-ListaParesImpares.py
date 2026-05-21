pares = [0,2,4,6,8]
impares = [1,3,5,7,9]
num = []
listaTotPar = []
listaTotImp = []
for i in range(1,8):
    valor = int(input(f'Digite o {i} valor: '))
    num.append(valor)
    if valor % 2 == 0:
        listaTotPar.append(num[:])
    else:
        listaTotImp.append(num[:])
    num.clear()

print(f'Os valores pares digitados são: {listaTotPar}')

print(f'Os valores impares digitados são: {listaTotImp}')











