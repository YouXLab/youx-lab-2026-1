from operator import itemgetter

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
    {"Nome": "Carolina",  "Salario": 6000, "anos_trabalhados": 4},
    {"Nome": "Henrique",  "Salario": 5000, "anos_trabalhados": 6},
]

for i in funcionarios:
    print("-=" * 20)
    print('    ATUALIZANDO FUNCIONÁRIO', i["Nome"])
    if i["anos_trabalhados"] <= 5:
        i["novo_salario"] = i["Salario"] * 1.10
    elif i["anos_trabalhados"] > 5:
        i["novo_salario"] = i["Salario"] * 1.20
    print(f"Funcionário {i['Nome']}: salário antigo = {i['Salario']}, salário novo = {i['novo_salario']:.2f} ")

# plus: desconto inss
print("\n\nAGORA AQUI ESTÁ QUEM RECEBEU DESCONTOS REFERENTE A INSS:\n")
primeiro = [] # lista que registra funcionarios que recebeu o desconto de 7,5%
segundo = [] # 9%
terceiro = [] # 12%
quarto = [] # 14%

def calcular(salario, desconto):
    formula = desconto / 100
    desconto = (salario * (1 + formula)) - salario
    return float(desconto)

for i in funcionarios:
    novo =  i["novo_salario"]
    if novo <= 1621.00:
        i["desconto"] = novo - calcular(novo, 7.5)
        primeiro.append(i)
    elif novo <= 2902.84:
        i["desconto"] = novo - calcular(novo, 9)
        segundo.append(i)
    elif novo <= 4354.27:
        i["desconto"] = novo - calcular(novo, 12)
        terceiro.append(i)
    elif novo <= 8475.55:
        i["desconto"] = novo - calcular(novo, 14)
        quarto.append(i)


if len(primeiro) > 0:
    print('  OS QUE RECEBERAM 7.5% DE DECONTO FORAM:')
    for i in primeiro:
        print(f"    {i['Nome']}, seu salario final foi: {i['desconto']:.2f}")
if len(segundo) > 0:
    print('  OS QUE RECEBERAM 9% DE DECONTO FORAM:')
    for i in segundo:
        print(f"    {i['Nome']}, seu salario final foi: {i['desconto']:.2f}")
if len(terceiro) > 0:
    print('  OS QUE RECEBERAM 12% DE DECONTO FORAM:')
    for i in terceiro:
        print(f"    {i['Nome']}, seu salario final foi: {i['desconto']:.2f}")
if len(quarto) > 0:
    print('  OS QUE RECEBERAM 14% DE DECONTO FORAM:')
    for i in quarto:
        print(f"    {i['Nome']}, seu salario final foi: {i['desconto']:.2f}")



# Nome: XXX | Salario: XXX
novaLista = []
for i in funcionarios:
    dados = (i['desconto'], i['Nome'])
    novaLista.append(dados)

print('\nO RANKING FINAL ORDENADO PELO MAIOR SALARIO:')
ranking = sorted(novaLista, reverse=True)

for i in ranking:
    print(f'Nome: {i[1]} | Salario: {i[0]:.2f}')