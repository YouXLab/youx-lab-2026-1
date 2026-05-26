ficha = []

# 1. Leitura dos dados e armazenamento na lista composta
while True:
    nome = str(input("Nome do aluno: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2

    # Estrutura da lista: [nome, [nota1, nota2], media]
    ficha.append([nome, [nota1, nota2], media])

    resp = str(input("Quer continuar? [S/N] ")).strip().upper()
    if resp[0] == 'N':
        break

# 2. Exibição do Boletim
print("\n" + "-=" * 20)
print(f"{'Nº':<4}{'NOME':<15}{'MÉDIA':>8}")
print("-" * 35)
for i, aluno in enumerate(ficha):
    print(f"{i:<4}{aluno[0]:<15}{aluno[2]:>8.1f}")

# 3. Consulta de notas individuais
while True:
    print("-" * 35)
    opc = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if opc == 999:
        print("Finalizando...")
        break
    if opc <= len(ficha) - 1:
        print(f"Notas de {ficha[opc][0]} são: {ficha[opc][1]}")
    else:
        print("Aluno não encontrado! Tente novamente.")

