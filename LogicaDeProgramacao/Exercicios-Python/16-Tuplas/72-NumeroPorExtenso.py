N1 = int(input('Digite um numero de 0 a 20: '))
ext =('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    if N1 < 0:
        N1 = int(input('Numero inferior ao valor indicado. Digite um numero de 0 a 20: '))
    elif N1 > 20:
        N1 = int(input('Numero superior ao valor indicado. Digite um numero de 0 a 20: '))
    else:
        break
print(f'O numero escolhido foi: {ext[N1]}')