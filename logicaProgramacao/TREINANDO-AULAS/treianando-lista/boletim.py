# BOLETIM ESCOLAR
# Lista + Dicionário + FOR + média

alunos = []

for i in range(3):
    aluno = {}

    print(f"\nALUNO {i+1}")

    aluno["nome"] = input("Nome: ")

    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))

    media = (n1 + n2) / 2

    aluno["media"] = media

    if media >= 7:
        aluno["situacao"] = "Aprovado"
    else:
        aluno["situacao"] = "Reprovado"

    alunos.append(aluno)

print("\nBOLETIM")
print("-" * 30)

for a in alunos:
    print(f"Nome: {a['nome']}")
    print(f"Média: {a['media']:.1f}")
    print(f"Situação: {a['situacao']}")
    print("-" * 30)