#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média
#entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
from math import inf

soma = 0
quantidade = 0
maior = float('-inf')
menor = float('inf')
resposta = 's'
while resposta != 'n':
    n = float(input('Digite um numero: '))
    soma = soma + n
    quantidade = quantidade + 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    resposta =input('Você deseja digitar outro numero [S/N]? ').lower()

media = soma / quantidade
print(f'Voce digitou {quantidade} numeros e a media foi {media} o maior valor foi {maior} e o menor {menor}')

print(f'quantidade ={quantidade}')
print(f'media = {media}')
print(f'maior = {maior}')
print(f'menor = {menor}')
