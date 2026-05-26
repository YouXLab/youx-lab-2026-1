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
novo_salario = [] #criei uma lista para guardar os novos salarios

for f in funcionarios: #para cada funcionario(usei só o f para não confundir) em funcionarioS
    salario_antigo = f["Salario"] #criei uma variavel para receber o salario antigo que esta dentro do dicionario

    if f["anos_trabalhados"] > 5: #se os anos trabalhados forem maiores que 5
        novo_salario = salario_antigo * 1.2 #criei uma nova variavel que vai receber salario antigo * 1.2(porque? ao inves de fazer salario antigo + salario * 20 / 100 fiz assim, salario antigo * 1 salario completo + 20%)
    else: #senão
        novo_salario = salario_antigo * 1.1 #mesma coisa que o de cima com diferença que não é 20% mas sim 10%

    print(f"Funcionário {f['Nome']}: salário antigo = {salario_antigo}, salário novo = {novo_salario:.2f}")
#por fim,printei "Nome",a variavel criada anteriormente salario_antigo e a variavel novo_salario por fim...

#dificuldade:
#Pensar como criar o For (Sei como funcina mas as vezes é complicado cria-lo)































