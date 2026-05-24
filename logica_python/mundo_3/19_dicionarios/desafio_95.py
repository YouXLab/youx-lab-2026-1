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