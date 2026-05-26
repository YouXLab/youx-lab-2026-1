funcionarios = [
    {'nome': 'Ana', 'salario': 1500, 'aumento': 10},
    {'nome': 'Carlos', 'salario': 2300, 'aumento': 15},
    {'nome': 'Beatriz', 'salario': 3200, 'aumento': 8}
]

for f in funcionarios:
    novo = f['salario'] + (f['salario'] * f['aumento'] / 100)
    f['novo_salario'] = novo

print('RELATÓRIO DOS FUNCIONÁRIOS')

for f in funcionarios:
    print('-' * 30)
    print(f'Nome: {f["nome"]}')
    print(f'Salário antigo: R$ {f["salario"]:.2f}')
    print(f'Aumento: {f["aumento"]}%')
    print(f'Novo salário: R$ {f["novo_salario"]:.2f}')