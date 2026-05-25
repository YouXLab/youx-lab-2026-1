#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista
# composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa
# mostrar as notas de cada aluno individualmente.


alunos = []
continuar = "S"
while continuar != "N":
    nome = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    continuar = input("Quer continuar? [S/N] ").upper()
print("-=" * 20)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, aluno in enumerate(alunos):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
opcao = 0
while opcao != 999:
    print("-=" * 20)
    opcao = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if opcao <= len(alunos) - 1 and opcao != 999:
        print(f'Notas de {alunos[opcao][0]} são {alunos[opcao][1]}')
