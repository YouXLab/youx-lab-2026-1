valores = []
num_par = 0
num_impar = 0
impar = []
par = []
for c in range(0,7):
    numero = int(input(f'Digite o {c+1}º valor: '))
    if numero % 2 == 0:
        num_par = numero
        par.append(num_par)
    if numero % 2 != 0:
        num_impar = numero
        impar.append(num_impar)
print('≃'*30)
print(f'Os valores pares digitados foram: {sorted(par)}')
print(f'Os valores impares digitados foram: {sorted(impar)}')