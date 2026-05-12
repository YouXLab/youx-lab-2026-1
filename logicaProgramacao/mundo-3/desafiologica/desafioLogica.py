funcionarios = [['José', 1500, 6], ['Maria', 2200, 3], ['Everton', 3000, 5]]
novo_salario = []
final = []
for f in range(0, len(funcionarios)):
    if funcionarios[f][2] <= 5:
        novo = funcionarios[f][1] + (funcionarios[f][1] * 10/100)
        novo_salario.append(funcionarios[f][0])
        novo_salario.append(novo)
        novo_salario.append(funcionarios[f][2])
        final.append(novo_salario[:])
        novo_salario.clear()
    elif funcionarios[f][2] > 5:
        novo = funcionarios[f][1] + (funcionarios[f][1] * 20 / 100)
        novo_salario.append(funcionarios[f][0])
        novo_salario.append(novo)
        novo_salario.append(funcionarios[f][2])
        final.append(novo_salario[:])
        novo_salario.clear()
for f, s in enumerate(final):
    print(f'Funcionario {final[f][0]}: salario antigo {funcionarios[f][1]} => novo salario {s}')

print(final)