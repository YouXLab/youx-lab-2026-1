galera = []
pessoa = {}
soma = media = 0

while True:
    # Leitura dos dados
    pessoa['nome'] = str(input('Nome: '))

    # Validação do sexo
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in ['M', 'F']:
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']

    # Adiciona a cópia do dicionário à lista
    galera.append(pessoa.copy())

    # Pergunta se deseja continuar
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in ['S', 'N']:
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

# Cálculos finais
total_pessoas = len(galera)
media = soma / total_pessoas

# A) Quantas pessoas cadastradas
print(f'\nA) Ao todo, temos {total_pessoas} pessoas cadastradas.')

# B) A média de idade
print(f'B) A média de idade é de {media:.2f} anos.')

# C) Uma lista com as mulheres
print('C) As mulheres cadastradas são: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()

# D) Lista de pessoas com idade acima da média
print('D) Lista de pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] > media:
        print(f'   => Nome: {p["nome"]}; Sexo: {p["sexo"]}; Idade: {p["idade"]} anos.')
