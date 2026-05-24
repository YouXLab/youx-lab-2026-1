time = []

# 1. ENTRADA DE DADOS
while True:
    nome = str(input('Nome do Jogador: ')).strip()
    tot = int(input(f'Quantas partidas {nome} jogou? '))

    # Gols com list comprehension (uma linha)
    gols = [int(input(f'   Quantos gols na partida {i + 1}? ')) for i in range(tot)]

    # Salva direto na lista
    time.append({
        'nome': nome,
        'gols': gols,
        'total': sum(gols)
    })

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()
        if resp in 'SN': break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N': break

# 2. CABEÇALHO E TABELA
print('-' * 45)
print(f'{"cod":<4} {"nome":<15} {"gols":<15} {"total":<5}')
print('-' * 45)

for k, v in enumerate(time):
    print(f'{k:<4} {v["nome"]:<15} {str(v["gols"]):<15} {v["total"]:<5}')
print('-' * 45)

# 3. SISTEMA DE BUSCA
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999: break

    if busca >= len(time) or busca < 0:
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        # Exibe detalhes do jogador selecionado
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
    print('-' * 45)

print('<< VOLTE SEMPRE >>')