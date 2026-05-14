# Exercício Python 055: Faça um programa que leia o peso
# de cinco pessoas. No final, mostre qual foi o maior e o
# menor peso lidos.

print('=========Maior e Menor=========')
lista = []
for variavel in range(0,5):
    peso = float(input(f'Quanto pesa a {1+variavel}° pessoa?:'))
    lista.append(peso)
print(f'O maior peso descrito foi:',max(lista), 'kg')
print(f'O menor peso descrito foi:',min(lista), 'kg')






