def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'COM {idade} ANOS DE IDADE VOCÊ: NÃO VOTA!'
    elif idade <= 17 < 18 or idade > 65:
        return  f"COM {idade} ANOS DE IDADE VOCÊ: VOTO OPICIONAL"
    else:
        return  f"COM {idade} ANOS DE IDADE VOCÊ: VOTA OBRIGATÓRIAMENTE"


#PROGRAMA PRINCIPAL
nascimento = int(input("EM QUE ANO VOCÊ NASCEU?:"))
print(voto(nascimento))




