from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
dados['nascimento'] = int(input('Ano de Nascimento: '))
dados['clt'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['clt'] != 0:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$'))
print('-='*30)
ano_atual = datetime.now().year
dados['idade'] = ano_atual - dados['nascimento']
dados['aposentadoria'] = (dados['contratacao'] + 35) - ano_atual + dados['idade']
for k, v in dados.items():
    print(f'{k} tem o valor de {v}')