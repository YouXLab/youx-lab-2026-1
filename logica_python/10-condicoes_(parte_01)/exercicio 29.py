velocidade = int(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    velocidade_acima = velocidade - 80
    preco_total_da_multa = velocidade_acima * 7
    print(f"Sua velocidade é {velocidade} km/h você foi multado em R${preco_total_da_multa}")
else:
    print(f"Velocidade:{velocidade} km/h")




