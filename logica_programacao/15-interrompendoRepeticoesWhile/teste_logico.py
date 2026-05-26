numero = soma = 0 # 'numero' e 'soma' começa em 0
while True: # enquanto for verdade (ou seja infinito entre muitas aspas)
    numero = int(input('DIGITE UM VALOR... --> ')) #'numero' recebe um número inteiro de input/pergunta
    if numero == 999: #se 'numero' for igual à 999
        break #PARA TUDO
    soma = soma + numero #após a digitação e o stop,faça 'soma' recebe 'soma' mais 'numero'
print(f'A SOMA VALE {soma}') #mostra soma de tudo


