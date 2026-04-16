#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import calendar
data = int(input("Em que ano voce esta? "))
if calendar.isleap(data):
    print("É bissexto")
else:
    print("Nao é bissexto")