from datetime import date
dados = {}
ano = date.today().year
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['idade'] = ano - nascimento
ctps = int(input('Carteira de trabalho: (0 não tem) '))
if ctps != 0:
    ano_contratacao = int(input('Ano de contratação: '))
    dados['contratação'] = ano_contratacao
    dados['salário'] = int(input('Salário: '))
    aposentadoria = (ano_contratacao-nascimento) + 35
    dados['aposentadoria'] = aposentadoria
print(' ')
for d, v in dados.items():
    print(f'{d} tem valor {v}')