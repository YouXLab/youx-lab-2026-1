"""nome = str(input('Qual é seu nome? '))
if nome == 'Thauany':
    print('Que nome bonito!')
elif nome == 'Vitória' or nome == 'Jheniffer' or nome == 'Aurora':
    print('Seu nome é bem popular no Brasil.')
else:
    print('Seu nome é bem normal.')
print(f"Tenha um bom dia, {nome}")"""



valor_da_casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do seu salário? '))
quantidade_de_anos_pagamento = int(input('Em quantos anos você vai pagar a casa? '))
quantidade_prestacoes = quantidade_de_anos_pagamento * 12
valor_prestacao = valor_da_casa / quantidade_prestacoes

if valor_prestacao < (salario * 0.3):
    print(f"Empréstimo aceito! Você irá pagar {quantidade_prestacoes} parcelas de  R$ {valor_prestacao:.2f}")
else:
    print('Empréstimo negado')

















