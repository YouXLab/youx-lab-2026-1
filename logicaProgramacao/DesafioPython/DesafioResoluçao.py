from logicaProgramacao.Mundo_3.utilidadecev.moeda import aumentar

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

for funcionario in funcionarios:        #usei o for para repetiçao de funcionarios para entrar dentro do dicionario.

    if funcionario ['anos_trabalhados'] > 5:   # usei if para colocar uma condiçao pois se for maior de 5 vai aumentar 20%
         aumentar = funcionario["Salario"] * 20/100
         funcionario["novo_salario"] = funcionario['Salario'] + aumentar
         print(f'O aumento do funcionario foi de {aumentar}')

    elif funcionario ['anos_trabalhados'] <= 5:             #usei elif para colocar uma condiçao pois se for menor ou igual a 5 de anos trabalho aumenta so 10%
        aumentar = funcionario["Salario"] * 10/100
        funcionario["novo_salario"] = funcionario['Salario'] + aumentar
        print(f'O aumento do funcionario foi de {aumentar}')

    print(f'Funcionario {funcionario['Nome']}  salario antigo {funcionario['Salario']}  salario novo: {funcionario['novo_salario']}')
#Muita dificuldade em acessar valor
# Dificuldade com sintaxe
# Dificuldade de testar
# Dificuldade de iniciar


