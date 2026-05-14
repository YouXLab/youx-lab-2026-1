termo = int(input('Primeiro termo: '))
razao = int(input('Número da razão: '))
decimo = termo + (10 - 1) * razao
for c in range (termo, decimo + razao, razao):
    print('{}'.format(c), end=' ')
print('ACABOU')


