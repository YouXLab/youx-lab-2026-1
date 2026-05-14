numero =int(input('digite um número: '))
primo = True
for c in range(2, numero):
    if (numero % c) == 0:
        primo = False

if primo:
    print('o numero é primo')
else:
    print('o numero nao é primo')
