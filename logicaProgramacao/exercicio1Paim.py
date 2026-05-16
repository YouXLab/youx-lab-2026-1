lista= []
funcionariosAjustes = []
funcionarios = [['Jose', 1500, 6], ['Maria', 2200, 3], ['Everton', 3000, 5]]
for nome, salario, anos in funcionarios:
    if anos > 5:
         novo_salario = salario + (salario * 20 / 100)
    else:
        novo_salario =  salario + (salario * 10 / 100)
    funcionariosAjustes.append([nome, novo_salario, anos ])
print(funcionariosAjustes)
for indice, pessoas in enumerate(funcionariosAjustes):
    print(f"O salario antigo de {funcionarios[indice][0]} =  R${funcionarios[indice][1]:.2f}, o atual é R${funcionariosAjustes[indice][1]:.2f}")