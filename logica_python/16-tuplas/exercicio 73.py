times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo',
         'Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza',
         'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco',
         'Bahia', 'Santos', 'Goiás', 'Coritiba', 'Chapecoense')

print(f"Os 5 primeiros times: {times[0:5]}")

print(f"Os últimos 4 colocados: {times[-4:]}")

print(f"Times em ordem alfabética: {sorted(times)}")

posicao = times.index('Chapecoense') + 1
print(f"A Chapecoense está na {posicao}ª posição.")

