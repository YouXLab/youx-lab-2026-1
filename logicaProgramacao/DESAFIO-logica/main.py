#REGRAS DO EXERCICIO!
#percorrer a uma lista usando FOR
#para cada funcionario,calcular o novo salario de acordo com a regra
#REGRA:trabalha 5 ou mais = 20% de aumento no salario
#5 anos ou menos = 10% de aumento no salario
#criar uma nova chave nomeada (novo_salario)
#fazer o print:  Funcionário José: salário antigo = 1500, salário novo = 1800.0


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
print('TABELA SALARIOS ATUALIZADA (aumentos)!!')
for funcionario in funcionarios:
#usando o for para percorrer a lista 'funcionarios'

    print('--' * 35)
    # deixar o codigo bonito

    salario = funcionario['Salario']
    # uma variavel que guarda o salario de cada funcionario
    #puxei da lista 'funcionarios' a informacao 'salario de cada um'

    tempo = funcionario['anos_trabalhados']
    # variavel que guarda os anos trabalhados de cada funcionario
    #vai puxar os anos trabalhados da lista nomeada 'funcionarios'

    if tempo > 5:
        aumento = salario * 1.20
    #se o tempo de trabalho for maior que 5 anos,aumento de 20% no salario

    else:
        aumento = salario * 1.10
    #se o tempo de trabalho for 5 anos ou menos,aumento de 10% no salario

    funcionario["novo_salario"] = aumento
    #uma nova chave com o nome 'novo_salario' que vai pegar o aumento de cada funcionario

    print(f"FUNCIONARIO:{funcionario['Nome']}, SALARIO ANTIGO:{funcionario['Salario']:.2f}, AUMENTO SALARIAL:{funcionario['novo_salario']:.2f}")
    #mostra na tela o nome de cada funcionario,seu salario antigo e seu salario atualizado

#travo na parte de 'começar' a ter a logica,se tiver alguem me ajudando consigo ir lembrando os comandos,se nao,esqueço e acabo travando.
#tenho dificuldade em criar uma logica boa,em fazer print puxando as informaçoes da lista,mexer com if/else.
#apesar de ter desenvolvido bem esse exercicio,creio q sem alguma  referencia talvez ficaria travada.
#DIFICULDADE:7/10
