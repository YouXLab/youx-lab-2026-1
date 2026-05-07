cadastros = dict()
while True:
    cadastros['nome'] = str(input('Nome: '))
    cadastros['média'] = float(input(f'Média de {cadastros["nome"]}: '))
    print('-='*10)
    if cadastros['média'] >= 6:
        cadastros['situação'] = 'Aprovado!'
    else:
        cadastros['situação'] = 'Reprovado!'
    break
print(f'Nome é igual a {cadastros["nome"]}\nMédia é igual a {cadastros["média"]}\nSituação é igual a {cadastros["situação"]}')