from datetime import datetime
dados = {}
dados['nome']=  str(input('Nome: '))
nascimento = int(input('Data de nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados ['ctps'] = int(input('Carteira de trabalho (0 nao tem): '))
if dados['ctps'] != 0:
    dados['contrataçao'] =int(input('Ano de contrataçao: '))
    dados['salario'] = float(input('Salario: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contrataçao'] + 35) - datetime.now().year)

92