funcionarios = [
    ['José', 1500, 6],
    ['Maria', 2200, 3],
    ['Everton', 3000, 5],
    ['Ana', 1800, 8],
    ['Carlos', 2500, 2],
    ['Fernanda', 3200, 7],
    ['Ricardo', 1700, 4],
    ['Patrícia', 2800, 9],
    ['Bruno', 1400, 1],
    ['Juliana', 3500, 11],
    ['Marcos', 2100, 5],
    ['Tatiane', 1900, 3],
    ['Diego', 2700, 6],
    ['Camila', 3100, 2],
    ['Rafael', 2000, 10],
    ['Aline', 1600, 4],
    ['Thiago', 2900, 7],
    ['Sabrina', 1750, 3],
    ['Leonardo', 3300, 12],
    ['Priscila', 2400, 5],
    ['Gustavo', 1850, 6],
    ['Vanessa', 2600, 1],
    ['Felipe', 3000, 8],
    ['Larissa', 1950, 4],
    ['Anderson', 2750, 9],
    ['Bruna', 1650, 2],
    ['Rodrigo', 3400, 13],
    ['Mariana', 2050, 5],
    ['Henrique', 2850, 7],
    ['Letícia', 1550, 3],
    ['Alexandre', 3150, 6],
    ['Renata', 2350, 4],
    ['Fábio', 2650, 10],
    ['Daniela', 1700, 2],
    ['Vinícius', 3050, 8],
]

novo_funcionarios = []
novo_salario = 0
for i in funcionarios:
    if i[2] > 5:
        novo_salario = (i[1] * 1.2)
        novo_funcionarios.append([i[0], novo_salario, i[2]])
    elif i[2] <= 5:
        novo_salario = (i[1] * 0.1) + i[1]
        novo_funcionarios.append([i[0], novo_salario, i[2]])
for e, j in enumerate(novo_funcionarios):
    print(f'Funcionário {j[0]}: salário antigo = {funcionarios[e][1]}, salário novo = {j[1]}')