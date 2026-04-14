dias = float(input("Quantos dias você ficou com o carro?: "));
km = float(input("Digite a quantidade de kms rodados: "));
total = (dias * 60) + (km * 0.15);
print("O total do aluguel foi de: R$", total)