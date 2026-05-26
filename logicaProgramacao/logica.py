#Conversor de temperatura
#Converter:
#Celsius → Fahrenheit
#Fahrenheit → Celsius
#Depois:
#transforme em menu interativo

temperatura = float(input("Digite a temperatura que será convertida: "))
conversor = float(input("[1] Celsius \n [2]Fahrenheit" ))
if conversor == 1:
    temperatura =  1.8 * temperatura + 32
    print(f"A temperatura em  Fahrenheit {temperatura}")
if conversor ==2:
    temperatura =  (temperatura - 32) / 1.8
    print(temperatura)