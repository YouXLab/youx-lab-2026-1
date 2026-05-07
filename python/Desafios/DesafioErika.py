funcionarios = [['José', 1500, 6], ['Maria', 2200, 3], ['Everton', 3000, 5]]
reajuste = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for cont in range(0, 3):
    reajuste[cont][0] = funcionarios[cont][0]
    reajuste[cont][2] = funcionarios[cont][2]
    if funcionarios[cont][2] > 5:
        aumento = funcionarios[cont][1] + ((funcionarios[cont][1] * 20)/100)
        reajuste[cont][1] = aumento
    elif funcionarios[cont][2] <= 5:
        aumento = funcionarios[cont][1] + ((funcionarios[cont][1] * 10) / 100)
        reajuste[cont][1] = aumento
    print(f'Funcionário {funcionarios[cont][0]}: Salário antigo = {funcionarios[cont][1]}, Salário novo = {reajuste[cont][1]}')