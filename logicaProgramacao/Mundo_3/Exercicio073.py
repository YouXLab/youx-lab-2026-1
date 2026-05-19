times = ('Corinthias', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro o maior de todos', 'Flamengo', 'Vasco', 'Chapecoense', 'Atletico menor de todos',
         'Botafogo', 'Athetico-PR', 'Bahia', 'Sao Paulo', 'Fluminense', 'Sport Recife', 'Ec Vitoria', 'Coritiba', 'Avai',
         'Ponte Preta', 'Athetico-GO')
print('-=' * 15)
print(f'Lista de times do Brasileirao: {times}')
print('-=' * 15)
print(f'Os 5 primeiros sao times {times[0:5]}')
print('-=' *  15)
print(f'Os ultimos sao {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-=' * 15)
print(f'O cruzeiro o maior de todos esta na {times.index("Cruzeiro o maior de todos")} posiçao')