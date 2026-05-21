pessoa = dict()
soma = media = 0
galera = []
total = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Digite o nome: '))
    while True:
        sexo = str(input('Digite o sexo: [M/F]')).upper().strip()
        if sexo in 'MF':
            pessoa['sexo'] = sexo
            break
        print('Erro! Responda [M/F]')
    pessoa['idade'] = int(input('Digite a idade: '))
    soma += pessoa['idade']
    total += 1
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()
        if resp in 'SN':
            break
        print('Erro! Responda [S/N]')
    if resp in 'N':
        break
print('-='*30)
print(f'A) Ao todo temos {total} pessoas.')
media = soma / total
print(f'B) A media de idades é: {media} anos')
print(f'C) As mulheres cadastradas são: ')
for a in galera:
    if a['idade'] >= media:
        print('      ')
        for k,v in a.items():
            print(f'{k} = {v}; ',end='')
        print()
print('Fim.')