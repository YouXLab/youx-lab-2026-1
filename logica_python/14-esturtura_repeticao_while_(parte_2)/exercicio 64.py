quantidade = 0
n1 = 0
soma = 0
while n1 != 999:
    n1 = int(input('Digite um número: '))
    quantidade += 1
    if n1 != 999:
        soma += n1
print(quantidade - 1)
print(soma)
