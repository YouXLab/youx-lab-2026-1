ano_atual = int(input('Digite o ano atual: '))
ano_nascimento = int(input('Qual o ano em que você nasceu? '))
idade = ano_atual - ano_nascimento

if idade < 18:
    tempo_alistamento = 18 - idade
    print(f"Ainda faltam {tempo_alistamento} anos para se alistar ")
elif idade ==18:
    print(f"Você precisa se alistar esse ano ")
else:
    alistamento = idade - 18
    print(f"Já se passaram {alistamento} anos para se alistar")







