dados = {}

dados['nome'] = str(input('nome: '))

dados['media']= float(input(f"Media de {dados['nome']}: "))
if dados['media'] < 7:
    dados['situacao'] = 'Recuperaçao'
else:
    dados['situacao'] = 'Aprovado'

for chave, valor in dados.items():
    print(f'{chave} é igual a {valor}')