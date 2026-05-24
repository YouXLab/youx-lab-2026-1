
galera = []
soma = 0
resp = 'S'

while resp == 'S':
    pessoa = {}

    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo [M/F]: ').upper()
    pessoa['idade'] = int(input('Idade: '))

    soma += pessoa['idade']
    galera.append(pessoa)

    resp = input('Quer continuar? [S/N] ').upper()

media = soma / len(galera)

print('-=' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
print(f'A média de idade é {media:.2f} anos.')

print('Mulheres cadastradas:', end=' ')
for p in galera:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')

print('\nPessoas acima da média:')
for p in galera:
    if p['idade'] >= media:
        print(p)