resp = 's'
temp = []
princ = []
mai = men = 0
while resp == 's':
    temp.append(str(input('nome: ')))
    temp.append(float(input('nome: ')))
    if len(princ) == 0:
        mai = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
            princ.append((temp[:]))
            temp.clear()
            resp = str(input('quer continuar? [S/N]'))
            print('-=' * 30)
            print(f'ao todo, voce cadastrou {len(princ)} pessoas.')
            print(f'o maior peso foi de {mai}kg')
            for p in princ:
                if p[1] == mai:
                    print(f'[{p[0]}', end='')
                    print ()
                    print(f'o menor peso foi{men}kg')
                    temp.append(float(input('peso: ')))
if len(princ)== 0:
   mai = men = temp[1]
else:
    if temp[1] > mai:
       mai = temp[1]
princ.append(((temp[:])))
temp.clear()
resp = str(input('quer continuar? [S/N]'))
print('-=' * 30)
print(f'ao todo, voce cadastrou {len(princ)} pessoas. ')
print(f' o maior peso foi{mai}kg')
for p in princ:
    if p [1] == mai:
        print(f'[{p[0]}', end='')
        print()
        print(f'o menor peso foi {men}kg')
        for p in princ:
            if p [1] == men:
                print(f'[{p[0]}', end='')
