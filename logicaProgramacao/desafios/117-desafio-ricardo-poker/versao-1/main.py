import random

valores = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}
lvalores = []
lnaipes = ["♠","♦","♣", "♥"]
for i in valores:
    lvalores.append(i)


mao = []
while len(mao) < 2:
    random.shuffle(lvalores)
    random.shuffle(lnaipes)
    carta = (f"{lvalores[0]}", f"{lnaipes[0]}")
    if carta not in mao:
        mao.append(carta)

mesa = []
while len(mesa) < 5:
    random.shuffle(lvalores)
    random.shuffle(lnaipes)
    carta = (f"{lvalores[0]}", f"{lnaipes[0]}")
    if carta not in mesa and carta not in mao:
        mesa.append(carta)
print("-"*25)
print("  Cartas da mesa:")
print(mesa)
print("-"*25)
print("  Cartas da mão:")
print(mao)
def achados(dicionario):
    resposta = ""
    for i, e in enumerate(dicionario):
        if dicionario[e] == True:
            resposta = True
        elif resposta != True:
            resposta = False
    return resposta

def converter_valor(*cartas):
    resposta = []
    for i, e in enumerate(valores):
        for i, valor in enumerate(cartas):
            if valor == e:
                resposta.append(valores[f"{valor}"])
    return resposta


def verificar_flush(*cartas):
    naipes = {
        "♠": 0,
        "♦": 0,
        "♣": 0
    }
    cartasResposta = []
    valoresResposta = []
    for i, e in enumerate(cartas[0]):
        for co, naipe in enumerate(naipes):
            if e[1] == naipe:
                cartasResposta.append(e)
                naipes[naipe] += 1
    resposta = False
    for co, naipe in enumerate(naipes):
        if naipes[naipe] >= 5:
            for i in cartasResposta:
                if i[1] == naipe:
                    valoresResposta.append(converter_valor(i[0])[0])
            resposta = ["Flush", valoresResposta]
    return resposta


def verificar_straight(cartas):
    seq = []
    for co, carta in enumerate(cartas):
        seq.append(converter_valor(carta[0])[0])
    seq.sort()
    for i, e in enumerate(seq):
        seq.sort(reverse=True)
        if seq[i - 4] - seq[i] == 4:
            encontrados["straightEn"] = True
            break
    if encontrados["straightEn"] == True:
        print(["Straight", seq[i-4:5]])
    return False

quadras = {

}
tudo = mao + mesa
for i, carta in enumerate(tudo):
    vcarta = converter_valor(carta[0])[0]
    if vcarta in quadras:
        quadras[vcarta] += 1
    else:
        quadras[vcarta] = 1
vquadras = []
vfullhouse = []
encontrados = {
    "quadraEn": False,
    "fhEncontrado": False,
    "flushEn": False,
    "straightEn": False,
    "trincaEnco": False
}

for i in quadras:
    vquadras.append(i)
    if quadras[i] >= 4:
        vquadras = [i]*4
        encontrados["quadraEn"] = True
        print(["Quadra", vquadras])
        break
    elif quadras[i] >= 3:
        for si in quadras:
            if quadras[si] >= 2 and si != i:
                vfullhouse.append(si)
                vfullhouse.append(si)
                vfullhouse.append(si)
                vfullhouse.append(i)
                vfullhouse.append(i)
                encontrados["fhEncontrado"] = True
        if encontrados["fhEncontrado"]:
            print(["Full house", vfullhouse])

if not achados(encontrados):
    if verificar_flush(mao + mesa):
        encontrados["flushEn"] = True
        print(verificar_flush(mao + mesa))
if not achados(encontrados):
    if verificar_straight(mao + mesa):
        encontrados["straightEn"] = True
        print(verificar_straight(mao + mesa))
if not achados(encontrados):
    cartass = {

    }
    for i in tudo:
        if i[0] in cartass:
            cartass[i[0]] += 1
        else:
            cartass[i[0]] = 1
    for i in cartass:
        if cartass[i] >= 3:
            encontrados["trincaEnco"] = True
            print(["Trinca", i,i,i])
if not achados(encontrados):
    pares = {

    }
    par = []
    cartasPares = []
    for i in tudo:
        if i[0] in pares:
            pares[i[0]] += 1
        else:
            pares[i[0]] = 1
    for co, carta in enumerate(pares):
        if pares[carta] >= 2:
            for cont, valor in enumerate(pares):
                if pares[valor] >= 2 and valor != carta:
                    cartasPares.append(valor)
                    cartasPares.append(carta)
                elif pares[valor] >= 2:
                    par.append(valor)
    if len(cartasPares) >= 4:
            print(["Pares", cartasPares])
            encontrados["paresEncontrados"] = True
    elif len(pares) >= 1:
        if par:
            print(["Par", par, par])
            encontrados["parEncontrado"] = True
if not achados(encontrados):
    valoresConvertidos = []
    for i in tudo:
        valoresConvertidos.append(converter_valor(i[0]))
    valoresConvertidos.sort(reverse=True)
    print(["High card", valoresConvertidos[0]])