nome = str(input('Qual é seu nome? '));
if nome == 'Luiz':
    print('Que nome bonito!');
elif nome == 'Pedro' or nome == 'Joana' or nome == "Jõao":
    print('Seu nome é bem popular no Brasil!');
elif nome in 'Ana Cláudia Maria Jose':
    print('Que belo nome feminino!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}!'.format(nome));