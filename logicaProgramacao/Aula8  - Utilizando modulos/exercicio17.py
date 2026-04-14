#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math

cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))
cateto_oposto = float(input("Digite o valor do cateto oposto"))
hipotenusa = math.hypot(cateto_adjacente,cateto_oposto)
print(f"O valor da hipotenusa vai ser {hipotenusa:.2f}") 