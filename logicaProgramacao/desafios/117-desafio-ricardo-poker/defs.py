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



# funções (para deixr o código mais organizado):
def avaliar_mao(cartas):
    defs = [verificar_quadra, verificar_fullhouse, verificar_flush, verificar_straight]
    for i in defs:
        resposta = i(cartas)
        if resposta:
            return resposta
    valorescont = contar_valores(cartas)
    if not resposta:
        for i in valorescont:
            if valorescont[i] >= 3:
                resposta = ("Trinca", [i])
                return resposta
    if not resposta:
        for i in valorescont:
            if valorescont[i] >= 2:
                for k in valorescont:
                    if valorescont[k] >= 2 and k != i:
                        resposta = ("Pares", [i, k])
                        return resposta
    if not resposta:
        for i in valorescont:
            if valorescont[i] >= 2:
                resposta = ("Par", [i])
                return resposta
    if not resposta:
        valoresConvertidos = converter_valores(cartas)
        valoresConvertidos.sort(reverse=True)
        valoresConvertidos = [valor[0] for valor in valoresConvertidos]
        resposta = ("High cart", [valoresConvertidos[0]])
        return resposta


def converter_valores(cartas):
    resposta = []
    for carta in cartas:
        for valor in valores:
            if carta[0] == valor:
                resposta.append((valores[valor], carta[1]))
    return resposta

def contar_valores(cartasRecebidas):
    cartas = {}
    cartasRecebidas = converter_valores(cartasRecebidas)
    for i in cartasRecebidas:
        if i[0] in cartas:
            cartas[i[0]] += 1
        else:
            cartas[i[0]] = 1
    return cartas

def contar_naipes(cartasRecebidas):
    cartas = {}
    cartasRecebidas = converter_valores(cartasRecebidas)
    for i in cartasRecebidas:
        if i[1] in cartas:
            cartas[i[1]] += 1
        else:
            cartas[i[1]] = 1
    return cartas

def verificar_quadra(cartas):
    contagem = contar_valores(cartas)
    for i in contagem:
        if contagem[i] >= 4:
            return ("Quadra", [i])

def verificar_fullhouse(cartas):
    contagem = contar_valores(cartas)
    maiorTrinca = []
    maiorPar = []
    for i in contagem:
        if contagem[i] >= 3:
            maiorTrinca.append(i)
    if maiorTrinca:
        melhorTrinca = max(maiorTrinca)
        for valor in contagem:
            if valor != melhorTrinca and contagem[valor] >= 2:
                maiorPar.append(valor)
    if maiorPar and maiorTrinca:
            return ("Full house", [melhorTrinca, max(maiorPar)])

def verificar_flush(cartas):
    contagemNaipes = contar_naipes(cartas)
    cartasFlush = []
    naipe = ""
    for i in contagemNaipes:
        if contagemNaipes[i] >= 5:
            naipe = i
    if naipe != "":
        for i in cartas:
            if i[1] == naipe:
                cartasFlush.append(i)

    resposta = []
    for i in converter_valores(cartasFlush):
        resposta.append(i[0])
    resposta.sort(reverse=True)
    if resposta:
        return ("Flush", resposta[:5])

def ordem(cartas):
    valores = converter_valores(cartas)
    valorCartas = [v[0] for v in valores]
    valorCartas.sort()
    for i, e in enumerate(valorCartas):
        for k in valores:
            if k[0] == valorCartas[i]:
                valorCartas[i] = k
    return valorCartas
def verificar_straight(cartas):
    cartas = ordem(cartas)
    valores = [valor for valor in cartas]
    valoresExtraidos = []
    for i in valores:
        if i[0] not in valoresExtraidos:
            valoresExtraidos.append(i[0])
    for i in range(4, len(valoresExtraidos)):
        if valoresExtraidos[i] - 4 == valoresExtraidos[i - 4]:
            return ("Straight", valoresExtraidos[i-4:i+1])