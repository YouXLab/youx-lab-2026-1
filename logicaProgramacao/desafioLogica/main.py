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

for f in range(0, len(funcionarios)): # Percorre a lista
    if funcionarios[f]['anos_trabalhados'] > 5: # Verifica os anos de trabalho do funcionario
        funcionarios[f]['novo_salario'] = funcionarios[f]['Salario'] + (funcionarios[f]['Salario'] * 20/100) # Aplica o aumento de salario
    elif funcionarios[f]['anos_trabalhados'] <= 5: # Verifica os anos de trabalho do funcionario
        funcionarios[f]['novo_salario'] = funcionarios[f]['Salario'] + (funcionarios[f]['Salario'] * 10 / 100) # Aplica o aumento de salario
    print(f'Funcionario: {funcionarios[f]["Nome"]}, Salario antigo: {funcionarios[f]["Salario"]} -> Novo salario: {funcionarios[f]["novo_salario"]}') #Mostra os dados antigos e atualizados do funcionario

print('-'*30)

# desconto do inss
sete = []
nove = []
doze = []
quatorze = []


for f in range(0,len(funcionarios)):
    dados = {}
    if funcionarios[f]["novo_salario"] <= 1621:
        dados["nome"] = funcionarios[f]["Nome"]
        dados["salario"] = funcionarios[f]["novo_salario"]
        dados["desconto"] = funcionarios[f]["novo_salario"] * 7.5/100
        sete.append(dados)
    elif funcionarios[f]["novo_salario"] >= 1621.01 and funcionarios[f]["novo_salario"] <= 2902.84:
        dados["nome"] = funcionarios[f]["Nome"]
        dados["salario"] = funcionarios[f]["novo_salario"]
        dados["desconto"] = funcionarios[f]["novo_salario"] * 9 / 100
        nove.append(dados)
    elif funcionarios[f]["novo_salario"] >= 2902.85 and funcionarios[f]["novo_salario"] <= 4354.27:
        dados["nome"] = funcionarios[f]["Nome"]
        dados["salario"] = funcionarios[f]["novo_salario"]
        dados["desconto"] = funcionarios[f]["novo_salario"] * 12 / 100
        doze.append(dados)
    elif funcionarios[f]["novo_salario"] >= 4354.28 and funcionarios[f]["novo_salario"] <= 8475.55:
        dados["nome"] = funcionarios[f]["Nome"]
        dados["salario"] = funcionarios[f]["novo_salario"]
        dados["desconto"] = funcionarios[f]["novo_salario"] * 14 / 100
        quatorze.append(dados)


print('7%')
for f in sete:
    print(f'Nome: {f["nome"]} Salario: {f["salario"]:.2f} Desconto: {f["desconto"]:.2f}')
print(' ')
print('9%')
for f in nove:
    print(f'Nome: {f["nome"]} Salario: {f["salario"]:.2f} Desconto: {f["desconto"]:.2f}')
print(' ')
print('12%')
for f in doze:
    print(f'Nome: {f["nome"]} Salario: {f["salario"]:.2f} Desconto: {f["desconto"]:.2f}')
print(' ')
print('14%')
for f in quatorze:
    print(f'Nome: {f["nome"]} Salario: {f["salario"]:.2f} Desconto: {f["desconto"]:.2f}')

#Não tive dificuldades e os erros que apareceram consegui resolver com certa facilidade