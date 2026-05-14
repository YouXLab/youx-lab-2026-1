numero = int(input('Diga um número:'))
primo = True
for contagem in range(0,100):
    print(contagem)
for contagem in range(2, numero):
    if (numero % contagem) == 0:
        primo = False
if primo:
    print(f'O número {primo} é Priminho')
else:
    print('O número não é Priminho')









