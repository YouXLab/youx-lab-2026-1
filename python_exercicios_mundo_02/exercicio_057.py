#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.


sexo = str(input("Informe o seu sexo [F/M] : ")).strip().upper()
while sexo not in "FM":
    sexo = str(input("INVÁLIDO.Por favor informe o seu sexo [F/M] : ")).strip().upper()
print("SEXO REGISTRADO")
