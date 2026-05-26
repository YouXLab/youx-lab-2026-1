from datetime import date

# Obtém o ano atual dinamicamente
ano_atual = date.today().year

dados = {
    'nome': str(input('Nome: ')),
    'ano_nasc': int(input('Ano de Nascimento: ')),
    'ctps': int(input('Carteira de Trabalho (0 não tem): '))
}

# Calcula a idade do usuário
dados['idade'] = ano_atual - dados['ano_nasc']

if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$ '))

    # Cálculo da aposentadoria (idade em que vai se aposentar = idade + tempo restante)
    tempo_contribuicao = ano_atual - dados['contratacao']
    anos_faltantes = 35 - tempo_contribuicao

    # Se já contribuiu por 35 anos ou mais, aposenta de imediato
    if anos_faltantes < 0:
        anos_faltantes = 0

    dados['aposentadoria'] = dados['idade'] + anos_faltantes

print('-=' * 30)

# Exibe todos os dados armazenados
for k, v in dados.items():
    print(f'  - {k.capitalize()} tem o valor {v}')
