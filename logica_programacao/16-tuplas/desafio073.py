print('-='*150)
print('Lista do Brasileirão em 2019')
print('-='*150)
times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR',
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás',
         'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará',
         'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('-='*150)
print(f'A lista de times do Brasileirão:{times}')
print('-='*150)
print(f'os primeiros 5 colocados foram:{times[0:5]}')
print('-='*150)
print(f'Os times que vão para a fase de grupo para a libertadores '
      f'são: {times[0:6]}')
print('-='*150)
print(f'os dois times que vão para a primeira fase da libertadores '
      f'são: {times[6:8]}')
print('-='*150)
print(f'Os times da sulamericana são {times[8:14]}')
print('-='*150)
print(f'Os times rebaixados foram{times[16:]}')
print('-='*150)
print(f'os times em ordem alfabética {sorted(times)}')
print('-='*150)
print(f'A chapecoense está na {times.index("Chapecoense")+1}ª posição')
print('-='*150)

#Essa eu não sei explicar mas...as informações estavam prontas peguei e as converti...um ponto interresante a destacar é o 'sorted' que é = organizar em ordem alfabetica...Além disso o ".index" foi usado para dizer em qual posição da range está os determinados itens...usei o +1 para não começar no zero,mas sim no 1(como começa no 0 quero q faça a contagem a partir do 1)



