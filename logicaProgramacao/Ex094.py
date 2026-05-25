pessoa = dict()
continuar = 'S'
galera = list()
soma = media = 0
while continuar == 'S':
    pessoa.clear()
    pessoa['nome'] = str(input('Digite o nome: '))
    pessoa['sexo'] = str(input('Digite o sexo [M/F]: ')).upper()[0]
    if pessoa['sexo'] not in 'MF':
        print('Digite seu sexo exato por favor! [M ou F]')
        pessoa['sexo'] = str(input('Digite o sexo [M/F]: ')).upper()[0]
    pessoa['idade'] = int(input('Digite a idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    continuar = str(input('Deseja continuar [S/N]: ')).upper()[0]
    while continuar not in 'SN':
        print('Esta errado,digite sim ou nao!')
        continuar = str(input('Deseja continuar [S/N]: ')).upper()[0]
if continuar == 'N':
    media = soma / len(galera)
    print('-=' * 10)
    print(f'A) Ao todos temos {len(galera)} pessoas cadastradas')
    print('-=' * 10)
    print(f'B) A media da idade das pessoas e {media:5.2f}')
    print('-=' * 10)
    print('C) As mulheres cadastradas foram',end=' ')
    for p in galera:
        if p['sexo'] == 'F':
            print(f'{p["nome"]}',end=',')
    print()
    print('-=' * 10)
    print('D) A Lista de pessoas acima da media:',end=' ')
    for p in galera:
        if p['idade'] > media:
            print('    ')
            for k,v in p.items():
                print(f'{k} = {v}',end=' , ')
            print()