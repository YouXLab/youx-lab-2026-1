#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
from urllib import response

lista = []
lista_pessoas = []
maior_peso = 0
menor_peso = 0
contador_pessoas = 0
resposta = ''
while 'N'not in resposta:
    lista_pessoas.append(input("Digite seu nome: "))
    lista_pessoas.append(float(input("Digite seu peso(Kg): ")))
    if len(lista_pessoas) == 0:
        maior_peso = menor_peso = lista_pessoas[1]
    else:
        if lista_pessoas[1] > maior_peso:
          maior_peso = lista_pessoas[1]
        if lista_pessoas[1] < menor_peso:
          menor_peso = lista_pessoas[1]
    lista.append(lista_pessoas[:])
    lista_pessoas.clear()
    resposta = input("Deseja continuar?[S/N] ").upper()
print(f" O numero total de pessoas cadastradas é {len(lista)} \n O maior peso sera {maior_peso:.1f}Kg e o menor sera {menor_peso:.1f}Kg ")

