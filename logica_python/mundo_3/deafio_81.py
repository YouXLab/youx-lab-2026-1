# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista

r = 's'
valores = []
while r == 's':
    valores.append(int(input('digite um valor: ')))
    r = input('quer continuar? [S/N]').upper()

print('-=' * 30)
print(f'voce digitou {len(valores)} elementos. ')

valores.sort(reverse=True)
print(f'os valores em ordem decrescente sao {valores}')
if 5 in valores:
    print('o valor 5 faz parte da lista!')
else:
    print('o valor 5 nao foi encontrado na lista!')
