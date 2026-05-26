print("-=_"*30)
print("SISTEMA FALIDO DO GOVERNO...TRIMESTRAL...MÉDIA É 18 PARA APROVAÇÃO...")
print("-=_"*30)
dicionario = dict()
dicionario["nome"] = str(input('QUAL O NOME DO|A ALUNO|A?: '))
dicionario["nota"] = float(input('QUAL A NOTA?: '))
print("_"*90)
print(f'O NOME É {dicionario["nome"]}')
print(f"A NOTA É {dicionario["nota"]}")
print("_"*90)
if dicionario["nota"]< 18:
    print('REPROVADIS')
else:
    print('APROVADIS')
print("_"*90)



