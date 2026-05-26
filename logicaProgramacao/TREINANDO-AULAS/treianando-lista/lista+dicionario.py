funcionarios = []

for trabalhador in range(1,4):
    dados = {}

    dados['nome'] = input(f'Nome do {trabalhador}º funcionário: ')
    dados['salario'] = float(input('Salário: R$ '))
    dados['aumento'] = float(input('Percentual de aumento: '))

    novo = dados['salario'] + (dados['salario'] * dados['aumento'] / 100)

    dados['novo_salario'] = novo

    funcionarios.append(dados)

print('\nRELATÓRIO DOS FUNCIONÁRIOS')

for f in funcionarios:
    print('-' * 30)
    print(f'Nome: {f["nome"]}')
    print(f'Salário antigo: R$ {f["salario"]:.2f}')
    print(f'Aumento: {f["aumento"]}%')
    print(f'Novo salário: R$ {f["novo_salario"]:.2f}')

#lista → funcionarios
# dicionário → dados
# cadastro de 3 salários
# cálculo de aumento em porcentagem.