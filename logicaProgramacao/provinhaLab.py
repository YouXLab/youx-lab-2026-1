
funcionarios = [
    {"Nome": "José",      "Salario": 1500, "anos_trabalhados": 6},
    {"Nome": "Maria",     "Salario": 1800, "anos_trabalhados": 4},
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
    {"Nome": "Carolina",  "Salario": 2050, "anos_trabalhados": 4},
    {"Nome": "Henrique",  "Salario": 2500, "anos_trabalhados": 6},
]

novo_salario = 0
for pessoa in range  (0, len(funcionarios)):
    if funcionarios[pessoa]['anos_trabalhados'] >= 5:
        novo_salario = funcionarios[pessoa]["Salario"] + (funcionarios[pessoa]["Salario"] * 20 / 100)
        funcionarios[pessoa]["novo_salario"] = novo_salario
    else:
        novo_salario = funcionarios[pessoa]["Salario"] + (funcionarios[pessoa]["Salario"] * 10 / 100)
        funcionarios[pessoa]["novo_salario"] = novo_salario
    print(f"O salario antigo de {funcionarios[pessoa]["Nome"]} é {funcionarios[pessoa]["Salario"]} o novo será {funcionarios[pessoa]["novo_salario"]}")
#dificuldade 3/10


#PLUS DESCONTO INSS
desconto7 = []
desconto9 = []
desconto12 = []
desconto14 = []
inss = 0
for pessoa in range(0, len(funcionarios)):
    if funcionarios[pessoa]['novo_salario'] >= 1621.01 and funcionarios[pessoa]['novo_salario']  <= 2902.84:
        inss = funcionarios[pessoa]['novo_salario'] - (funcionarios[pessoa]['novo_salario'] * 9 / 100)
        funcionarios[pessoa]['novo_salario'] = inss
        desconto9.append(funcionarios[pessoa])
    elif funcionarios[pessoa]['novo_salario'] >= 2902.85 and funcionarios[pessoa]['novo_salario']  <= 4354.27:
        inss = funcionarios[pessoa]['novo_salario'] - (funcionarios[pessoa]['novo_salario'] * 12 / 100)
        funcionarios[pessoa]['novo_salario'] = inss
        desconto12.append(funcionarios[pessoa])
    elif funcionarios[pessoa]['novo_salario'] >= 4354.28 and funcionarios[pessoa]['novo_salario']  <= 8475.55:
        inss = funcionarios[pessoa]['novo_salario'] - (funcionarios[pessoa]['novo_salario'] * 14 / 100)
        funcionarios[pessoa]['novo_salario'] = inss
        desconto14.append(funcionarios[pessoa])
    elif funcionarios[pessoa]['novo_salario'] <= 1621:
        inss = funcionarios[pessoa]['novo_salario'] - (funcionarios[pessoa]['novo_salario'] * 7.5 / 100)
        funcionarios[pessoa]['novo_salario'] = inss
        desconto7.append(funcionarios[pessoa])
#DIFICULDADE 4/10

#PLUS 2
#Nome: XXXX | Salario: XXX
ranking = []
pos = 0
for  pessoa in enumerate(funcionarios):
    if funcionarios[pessoa]["Salario"] > funcionarios[pessoa[pos]]["Salario"]:
        ranking.append(funcionarios[pessoa]['Salario'])
        pos+= 1
print(ranking)


        #print(f"Nome:{funcionarios[pessoa]['Nome']} | Salario: {funcionarios[pessoa]['Salario']}")









