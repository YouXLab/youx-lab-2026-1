ordem = ('Palmeiras', 'Flamengo', 'Fluminense', 'São Paulo', 'Athletico-PR', 'Bahia', 'Coritiba', 'Botafogo',
         'Bragantino', 'Vasco da Gama', 'Grêmio', 'Cruzeiro', 'EC Vitória', 'Corinthians', 'Atlético-MG',
         'Internacional', 'Santos', 'Mirassol', 'Remo', 'Chapecoense')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {ordem}')
print('-=' * 15)
print(f'Os 5 primeiros são {ordem[:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {ordem[16:20]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(ordem)}')
print('-=' * 15)
print(f'O Chapecoense está {ordem.index("Chapecoense")+1}° posição')
print('-=' * 15)