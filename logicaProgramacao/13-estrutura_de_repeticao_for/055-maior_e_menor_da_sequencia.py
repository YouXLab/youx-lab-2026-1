lista = []
for c in range(0, 5):
    peso = float(input('quanto você pesa: '))
    lista.append(peso)
print(f'o menor peso digitado',min(lista))
print(f'o maior peso digitado foi',max(lista))
