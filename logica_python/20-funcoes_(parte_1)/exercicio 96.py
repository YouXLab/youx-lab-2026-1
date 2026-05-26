def área(largura, comprimento):
    area_total = largura * comprimento
    print(f"A área de um terreno {largura}m x {comprimento}m é de {area_total}m².")

print("  Controle de Terrenos  ")
print("-" * 25)
l = float(input("LARGURA (m): "))
c = float(input("COMPRIMENTO (m): "))
área(l, c)
