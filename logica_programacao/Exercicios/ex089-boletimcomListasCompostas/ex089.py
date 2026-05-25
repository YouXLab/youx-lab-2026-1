lista = []
cont = 0
opcao = ''
while 'N' not in opcao:
    lista.append([])
    lista[cont].append(input("Digite o nome do aluno: "))
    lista[cont].append(float(input("Digite a nota do aluno: ")))
    lista[cont].append(float(input("Digite a segunda nota do aluno: ")))
    media = (lista[cont][1] + lista[cont][2]) / 2
    lista[cont].append(media)
    opcao = input("Deseja cadastrar a nota de mais algum aluno?[S/N] ").upper()
    cont += 1
print(f"{'No.':<6}{'NOME':<10}{'MEDIA':>6}")
for indice, aluno in enumerate (lista):
    print(indice, f"{aluno[0]:<15}  {aluno[3]:.1f}")

while aluno != 999:
    aluno = int(input("Voce deseja ver as notas de qual aluno? (Digite 999 para parar) \n"))
    print(f"As notas do {lista[aluno][0]} foram {lista[aluno][1:3]}")
print("Encerrando programa! \nVolte sempre")
