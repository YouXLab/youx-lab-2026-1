#Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
# de Futebol, na ordem de colocação. Depois mostre:

#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.


classificacao_brasileirao = (
    "Palmeiras",
    "Flamengo",
    "Fluminense",
    "São Paulo",
    "Athletico-PR",
    "Bragantino",
    "Bahia",
    "Coritiba",
    "Botafogo",
    "Atlético-MG",
    "Internacional",
    "Cruzeiro",
    "Santos",
    "Grêmio",
    "Vasco",
    "Vitória",
    "Corinthians",
    "Mirassol",
    "Remo",
    "Chapecoense"
)
#classificacao_5_primeiros = ("Palmeras","Flamengo","Fluminense","Sao Paulo",)
print("Os cinco primeiros colocados são: ", end='')
for i in range (0, 5):
    print(classificacao_brasileirao[i], end=' -> ')
print()

print("Os quatro últimos colocados são: ", end='')
for c in range(19, 15, -1):
    print(classificacao_brasileirao[c], end=' -> ')
print()

print("A lista dos times em ordem alfabética é: ")
timesOrdemAlfabetica = sorted(classificacao_brasileirao)
for time in timesOrdemAlfabetica:
    print(f"- {time}")
print()

print("Em que posição está o time da Chapecoense: ", end='')
print(f"{classificacao_brasileirao.index("Chapecoense") + 1}º posição ")
