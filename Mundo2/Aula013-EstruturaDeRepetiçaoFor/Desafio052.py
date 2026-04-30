#Faça um programa que leia um numero inteiro e diga se ele é ou nao um numero primo.

numero = int(input('Digite um numero: '))
eh_primo = True

for n in range(2, numero):
    if((numero % n) == 0):
        eh_primo = False

if(eh_primo):
    print('O numero digitado é primo')
else:
    print('O numero digitado nao é primo')

