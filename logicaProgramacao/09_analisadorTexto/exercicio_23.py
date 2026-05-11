numero= int(input('esse numero é'))
unidade= numero// 1 % 10
dezena= numero// 10 % 10
centena= numero// 100 % 10
milhar=numero// 1000 % 10
print(f'analisando o numero {numero}')
print(f'unidade: {unidade}')
print(f'dezena: {dezena}')
print(f'centena: {centena}')
print(f'milhar: {milhar}')