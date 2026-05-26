funcionarios = []

for c in range(3):
    dados = {}

    dados['nome'] = input('Nome: ')
    dados['salario'] = float(input('Salário: R$ '))

    funcionarios.append(dados)

print(funcionarios)

funcionarios = [
    {'nome': 'Ana', 'salario': 1500},
    {'nome': 'Carlos', 'salario': 2200},
    {'nome': 'Maria', 'salario': 3000}
]

for f in funcionarios:
    print(f'Nome: {f["nome"]}')
    print(f'Salário: R$ {f["salario"]:.2f}')
    print('-' * 20)

funcionarios = [
    {'nome': 'João', 'salario': 2000},
    {'nome': 'Lucas', 'salario': 3500},
    {'nome': 'Ana', 'salario': 1800}
]

for f in funcionarios:
    novo = f['salario'] + (f['salario'] * 10 / 100)

    print(f'Funcionário: {f["nome"]}')
    print(f'Novo salário: R$ {novo:.2f}')
    print('-' * 25)