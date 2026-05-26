from datetime import datetime
dados = dict()
dados['nome'] = str(input('digite seu nome: '))
nascimento = int(input('digite seu ano de nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('carteira de trabalho (0 nao tem):'))
if dados['ctps'] != 0:
    dados['contrataçao'] = int(input('ano de contrataçao: '))
    dados['salario'] = float(input('salario R$: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contrataçao'] + 35) - datetime.now(). year)
print(' =>' * 30)
for k, v in dados.items():
    print(f' -{k} tem o valor {v}')