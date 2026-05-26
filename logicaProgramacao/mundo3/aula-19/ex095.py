from itertools import count

lista_jogadores = []
resposta = 'S'
while resposta == 'S':
    jogador = {}
    partidas = []
    jogador['nome'] = input('Nome do jogador: ')
    total = int(input('Quantas partidas o jogador jogou no total? '))
    for c in range(0, total):
        partidas.append(int(input(f'   Quantos gols na partida {c}? ')))
        jogador['gols'] = partidas[:]
        jogador['total'] = sum(partidas)
    lista_jogadores.append(jogador)
    resposta = str(input('Deseja continuar? [s/n]')).upper()

print('~' * 30)
print('cod nomes',          'gols',          'total')
print('-=' * 20)
for cont, dado in enumerate(lista_jogadores):
    print(cont, end=' ')
    for caractere in dado:
        print(dado[caractere], end=" ")
    print()
opcao = 0
while opcao != 999:
    opcao = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if opcao == 999:
        print('FIM!')
    else:
        print(f'-- Levantamento do jogador: {lista_jogadores[opcao]["nome"]}')
        for cont, i in enumerate(lista_jogadores[opcao]["gols"]):
           print(f'no jogo {cont+1} fez {i} gols')
