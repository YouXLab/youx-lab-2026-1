funcionarios = [
    {"Nome": "José",      "Salario": 600, "anos_trabalhados": 6},
    {"Nome": "Maria",     "Salario": 700, "anos_trabalhados": 4},
    {"Nome": "João",      "Salario": 2200, "anos_trabalhados": 8},
    {"Nome": "Ana",       "Salario": 2000, "anos_trabalhados": 3},
    {"Nome": "Carlos",    "Salario": 2500, "anos_trabalhados": 10},
    {"Nome": "Paula",     "Salario": 2300, "anos_trabalhados": 5},
    {"Nome": "Marcos",    "Salario": 1900, "anos_trabalhados": 2},
    {"Nome": "Fernanda",  "Salario": 2600, "anos_trabalhados": 7},
    {"Nome": "Rafael",    "Salario": 2100, "anos_trabalhados": 4},
    {"Nome": "Clara",     "Salario": 2400, "anos_trabalhados": 6},
    {"Nome": "Bruno",     "Salario": 1700, "anos_trabalhados": 1},
    {"Nome": "Luiza",     "Salario": 2800, "anos_trabalhados": 9},
    {"Nome": "Felipe",    "Salario": 1950, "anos_trabalhados": 3},
    {"Nome": "Camila",    "Salario": 2250, "anos_trabalhados": 5},
    {"Nome": "Ricardo",   "Salario": 2700, "anos_trabalhados": 11},
    {"Nome": "Patrícia",  "Salario": 2100, "anos_trabalhados": 4},
    {"Nome": "Gustavo",   "Salario": 2600, "anos_trabalhados": 8},
    {"Nome": "Larissa",   "Salario": 1850, "anos_trabalhados": 2},
    {"Nome": "Tiago",     "Salario": 2350, "anos_trabalhados": 6},
    {"Nome": "Renata",    "Salario": 2550, "anos_trabalhados": 7},
    {"Nome": "Diego",     "Salario": 2000, "anos_trabalhados": 3},
    {"Nome": "Beatriz",   "Salario": 2450, "anos_trabalhados": 5},
    {"Nome": "André",     "Salario": 1900, "anos_trabalhados": 2},
    {"Nome": "Aline",     "Salario": 2300, "anos_trabalhados": 4},
    {"Nome": "Fábio",     "Salario": 2750, "anos_trabalhados": 9},
    {"Nome": "Sofia",     "Salario": 2150, "anos_trabalhados": 3},
    {"Nome": "Eduardo",   "Salario": 2650, "anos_trabalhados": 8},
    {"Nome": "Carolina",  "Salario": 5000, "anos_trabalhados": 4},
    {"Nome": "Henrique",  "Salario": 7000, "anos_trabalhados": 6},
]
for funcionario in funcionarios:
    if funcionario["anos_trabalhados"] > 5:
        aumento = funcionario["Salario"] + ((funcionario["Salario"] * 20)/100)
    elif funcionario["anos_trabalhados"] <= 5:
        aumento = funcionario["Salario"] + ((funcionario["Salario"] * 10) / 100)
    funcionario["novo_salario"] = aumento
    print(f'Funcionário {funcionario["Nome"]}: Salário antigo = {funcionario["Salario"]}, Salário novo = {aumento}')
print('-='*50)

#Plus desconto INSS

lista1 = list()
lista2 = list()
lista3 = list()
lista4 = list()
for inss in funcionarios:
    if inss["novo_salario"] <= 1621:
        desconto = inss["novo_salario"] - (inss["Salario"] * 7.5) / 100
        inss["pos_INSS"] = desconto
        lista1.append(inss)
        porcent = '7.5%'
    elif 1621.01 < inss["novo_salario"] < 2902.84:
        desconto = inss["novo_salario"] - (inss["Salario"] * 9) / 100
        inss["pos_INSS"] = desconto
        lista2.append(inss)
        porcent = '9%'
    elif 2902.85 < inss["novo_salario"] < 4354.27:
        desconto = inss["novo_salario"] - (inss["Salario"] * 12) / 100
        inss["pos_INSS"] = desconto
        lista3.append(inss)
        porcent = '12%'
    elif 4354.28 < inss["novo_salario"] < 8475.55:
        desconto = inss["novo_salario"] - (inss["Salario"] * 14) / 100
        inss["pos_INSS"] = desconto
        lista4.append(inss)
        porcent = '14%'
    print(f'Funcionário {inss["Nome"]}: Desconto: {porcent}, Salário após desconto do INSS: {inss["pos_INSS"]}')
