resp = None
valores = []
num_par = 0
num_impar = 0
impar = []
par = []
while resp != 'N':
    numero = int(input('Digite um número: '))
    resposta = str(input('Quer continuar? [S/N] '))
    resp = resposta.upper()
    valores.append(numero)
    if numero % 2 == 0:
        num_par = numero
        par.append(num_par)
    if numero % 2 != 0:
        num_impar = numero
        impar.append(num_impar)

    cont=len(valores)
   # print(cont)
print(f'Os números digitados foram {valores}.')
print(f'Os números ímpares foram {impar}')
print(f'Os números pares foram {par}.')