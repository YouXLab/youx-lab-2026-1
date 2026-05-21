temp = []
princ = []
maiorP = 0
menorP = 0
while True:
    temp.append(str(input('Nome:')))
    temp.append(float(input('Peso:')))
    if len(princ) == 0:
        maiorP = temp[1]
        menorP = temp[1]
    else:
        if menorP > temp[1]:
            menorP = temp[1]
        elif maiorP < temp[1]:
            maiorP = temp[1]

    princ.append(temp[:])
    temp.clear()
    SN = str(input('Quer continuar? [S/N] ').upper().strip())
    if SN == 'N':
        break

print(f'Ao todo você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {maiorP}. De ',end='')
for i in princ:
    if i[1] == maiorP:
        print(i[0],end=', ')
print()
print(f'O menor peso foi de {menorP}. De ',end='')
for i in princ:
    if i[1] == menorP:
        print(i[0],end=', ')
print()