jogadores = []
resposta = 'S'
while resposta == 'S':
    dados = {}
    gols_partida = []
    gols = 0
    dados['jogador'] = str(input('Nome: '))
    partidas = int(input('Quantas partidas ele(a) jogou? '))
    for i in range(0, partidas):
        gol = int(input(f"   Quantos gols {dados['jogador']} fez na partida {i + 1}°? "))
        gols_partida.append(gol)
        gols += gol
    dados['gols'] = gols_partida
    dados['total'] = gols
    jogadores.append(dados)
    resposta = str(input('Quer continuar? [S/N] ')).upper()
    while resposta not in 'NS':
        print('Resposta inválida. Tente novamente')
        continuar = str(input("Deseja  continuar? [S/N] ")).upper()
print('-='*30)
print(f'{'No.':<4}{'NOME':<10}{'GOLS':>10}{'TOTAL':<8}')
print('-'*26)
for i, a in enumerate(jogadores):
    print(f'{}')