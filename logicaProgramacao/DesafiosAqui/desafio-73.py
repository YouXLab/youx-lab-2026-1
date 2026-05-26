times = ('Palmeiras','Flamengo','Fluminense','São Paulo','Athletico-PR','Bahia','Red Bull Bragantino','Vasco da Gama','Coritiba','Vitória','Cruzeiro','Botafogo','Atlético-MG','Internacional','Santos','Corinthians','Grêmio','Mirassol','Remo','Chapecoense')

print(f"""≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃
Lista de times do Brasileirão: {times}
≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃""")
print(f'Os primeiros  5 colocados são: {times[0:5]}')
print(f"""≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃
Os últimos  4  colocados  são: {times [-4:]}
≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃""")
print(f'Em ordem alfabética: {sorted(times)}')
print('≃' * 30)
print(f'O Chapecoense está na {times.index("Chapecoense")+1} posição')
