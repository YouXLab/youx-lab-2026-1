from datetime import date
dados={}
dados["nome"] =input("nome: ")
nascimento = int(input('ano de nascimento: '))
dados['idade'] = date.today().year -nascimento
dados['ctps'] = int(input('ano de contratacao (0) nao tem: '))
if dados['ctps'] != 0:
    dados['contratacao']=int(input('ano de contratacao: '))
    dados['salario'] = float(input('salario: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) -date.today().year)
for k, v in dados.items():
    print(f'{k}: {v}')