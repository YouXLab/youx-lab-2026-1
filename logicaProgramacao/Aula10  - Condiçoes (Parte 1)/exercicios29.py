#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input("Qual a velocidade do seu carro? "))
multa = (velocidade - 80)
multa1 = multa * 7
if velocidade >= 81:
 print(f"Tomou multa otario, voce precisa pagar {multa1} de multa")
if velocidade >= 100:
 print("Voce vai morrer desse jeito")
else:
 print("Voce nao ultrapassou a velocidade permitida, dirija com cuidado")



