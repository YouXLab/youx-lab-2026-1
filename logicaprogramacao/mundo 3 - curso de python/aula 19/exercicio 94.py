galera = []
soma = 0
resp = 'S'
while resp == 'S':
    pessoa = {}
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo [M/F]: ').upper()[0]
    while pessoa['sexo'] not in 'MF':
        print('Erro! Digite apenas M ou F.')
        pessoa['sexo'] = input('Sexo [M/F]: ').upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    resp = input('Quer continuar? [S/N] ').upper()[0]
    while resp not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        resp = input('Quer continuar? [S/N] ').upper()[0]
media = soma / len(galera)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print()
print('D) Lista das pessoas que estão acima da média:')
for p in galera:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')