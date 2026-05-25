#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
# pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:

#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média


galera = list()
pessoa = dict()
soma = media = 0
resp = 'S'
while resp == 'S':
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = ' '
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if pessoa['sexo'] not in 'MF':
            print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp not in 'SN':
            print('ERRO! Responda apenas S ou N.')
