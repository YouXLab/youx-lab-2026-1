nome = str(input('Nome: '))
media = float(input(f'Media de {nome}: '))
if media < 7:
    situacao = 'Recuperaçao'
else:
    situacao = 'Aprovado'
dados = {
    'nome': nome,
    'media': media,
    'situacao': situacao
}
for chave, valor in dados.items():
    print(f'{chave} é igual a {valor}')
