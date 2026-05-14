cont = 1
soma= 0
while True:
    numero= int(input('digite um numero:'))
    if numero == 999:
      break
    soma += numero
    cont+=1
print(f'a soma dos {cont} foi {soma}')