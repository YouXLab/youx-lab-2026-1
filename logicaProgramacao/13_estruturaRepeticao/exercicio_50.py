soma= 0
cont= 0
for c in range (1, 7 ):
    numero= int(input(f'o numero é {c}'))
    if numero % 2 == 0:
         soma += numero
         cont += 1
print(f'o numero {cont} deu {soma}')



