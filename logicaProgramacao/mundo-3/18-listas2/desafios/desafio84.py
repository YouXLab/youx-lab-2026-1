dados = []
pessoas = []
resposta = 'S'
maior = menor = 0
while resposta == 'S':
    pessoas.append(str(input('Nome: ')))
    pessoas.append(int(input('Peso: ')))
    if len(dados) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        elif pessoas[1] < menor:
            menor = pessoas[1]
    dados.append(pessoas[:])
    pessoas.clear()
    resposta = str(input('Quer continuar? [S/N] ')).upper()
    while resposta not in 'SN':
        print('Resposta inválida. Tente novamente.')
        resposta = str(input('Quer continuar? [S/N] ')).upper()
print(f'Você cadastrou {len(dados)} pessoas.')
print(f'O maior peso é {maior}kg.')
print(f'O menor peso é {menor}kg.')