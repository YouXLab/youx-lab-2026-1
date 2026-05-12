dados = []
resposta = 'S'
soma = 0

while resposta == 'S':
    pessoa = {}
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    dados.append(pessoa)
    resposta = str(input('Quer continuar? [S/N] ')).upper()
    while resposta not in 'SN':
        print('Resposta inválida. Tente novamente.')
        resposta = str(input('Quer continuar? [S/N] ')).upper()
media = soma / len(dados)

print(f'O grupo tem {len(dados)} pessoas')
print(f'A média de idade é {media} anos')
print(f'As mulheres cadastradas foram: ', end='')
for s in dados:
    if s['sexo'] == 'F':
       print(s['nome'], end='')
print('')
print('Lista de pessoas com idade acima da media:')
for i in dados:
    if i['idade'] > media:
        print(f'Nome = {i['nome']}; sexo = {i['sexo']}; idade = {i['idade']}')