peso = float(input("Digite seu peso (kg): "));
al = float(input("Digite sua altura (m): "));
imc = peso / (al ** 2);
print("O imc dessa pessoa é {:.2f}".format(imc))
if imc < 18.5:
    print("Você está abaixo do peso indicado");
elif imc < 25:
    print("parabéns, você está em um peso ideal!")
elif imc < 30:
    print("Você está em sobrepeso");
elif imc < 40:
    print("Você está obeso");
elif imc > 40:
    print("Você está com obesidade mórbida!")