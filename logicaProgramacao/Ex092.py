infos = dict()
anos_restantes = 0
infos['nome'] = str(input('Digite o nome: '))
print('-='*10)
idadebeta = int(input('Digite o ano de nascimento: '))
infos['idade']= 2026 - idadebeta
infos['carteira'] = int(input('Digite a carteira de trabalho: '))
if infos['carteira'] != 0:
    infos['salario'] = float(input('Digite o salario: '))
    infos['ano'] = int(input('Digite o ano de contratacao: '))
    infos['calculo_anos'] = 2026 - infos['ano']
    infos['tempo_aposentar'] = 35 - infos['calculo_anos']
    if infos['tempo_aposentar'] <= 0:
        print('Voce ja esta aposentado')
    elif infos['tempo_aposentar'] > 0:
        soma_suprema = infos['idade'] + infos['tempo_aposentar']
        print(f'Nome e {infos['nome']}')
        print(f'Idade e {infos['idade']}')
        print(f'Ctps e {infos['carteira']}')
        print(f'Contratacao foi no ano de {infos['ano']}')
        print(f'Salario e {infos['salario']}')
        print(f'{infos["nome"]} vai aposentar com {soma_suprema}')