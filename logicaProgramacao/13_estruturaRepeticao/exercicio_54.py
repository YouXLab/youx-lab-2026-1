from datetime import date
atual= date.today().year
maior= 0
menor= 0
for c in range(1, 8):
    nascimento= int(input('data que nasceu'))
    idade= atual - nascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'tivemos {maior} maiores de idade')