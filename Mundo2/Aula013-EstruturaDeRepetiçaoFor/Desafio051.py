#PROGRESSAO ARITMETICA.
#Desenvolva um programa que leia o primeiro termo e a razao de uma PA.No final,mostre os primeiros termos dessa progressao.

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + primeiro, razao):
    print('{}'.format(c), end=' ')