times = ('Palmeiras', 'Flamengo', 'Fluminense', 'São Paulo', 'Athletico-PR', 'Bahia', 'Coritiba',
         'Botafogo', 'Bragantino', 'Vasco da Gama', 'Grêmio', 'Cruzeiro', 'EC Vitória', 'Corinthians',
         'Atlético-MG', 'Internacional', 'Santos', 'Mirassol', 'Remo', 'Chapecoense')

print('-=-'*15)
print(f'Lista de times do Brasileirão: {times}')
print('-=-'*15)
print(f'Os primeiros 5 times são: {times[: 5]}')
print('-=-'*15)
print(f'Os últimos 4 times são: {times[16: 20]}')
print('-=-'*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=-'*15)
print(f'O Chapecoense está {times.index("Chapecoense")+1}º posição')
print('-=-'*15)
