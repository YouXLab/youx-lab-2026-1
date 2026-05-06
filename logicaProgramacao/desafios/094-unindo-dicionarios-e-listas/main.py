dados = []
resposta = 'S'
mulheres = []
media = 0
soma = 0
while resposta == 'S':
    pessoas = {}
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('[M/F]: ')).upper()
    pessoas['idade'] = int(input('Idade: '))
    dados.append(pessoas)
    soma += pessoas['idade']
    resposta = str(input('Deseja continuar? [S/N] ')).upper()
    while resposta not in 'NS':
        print('Resposta inválida. Tente novamente')
        resposta = str(input("Deseja  continuar? [S/N] ")).upper()
print(f'Ao todo você cadastrou {len(dados)} pessoas.')
media = soma / len(dados)
print(f'A média de idade é {media} anos.')
for i in dados:
    if i['sexo'] == 'F':
        mulheres.append(i["nome"])
print(f'As mulheres cadastradas foram: ', end='')
for i in mulheres:
    print(f'{i}', end='; ')
print('')
print(f'Lista das pessoas que estão acima do média: ', end='')
for i in dados:
    if i['idade'] > media:
        print(f'Nome = {i['nome']}; Sexo = {i['sexo']}; Idade = {i['idade']};')