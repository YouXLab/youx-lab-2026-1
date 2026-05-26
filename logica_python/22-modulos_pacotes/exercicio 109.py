# ==========================================
# FUNÇÕES DO MÓDULO (Cálculos e Formatação)
# ==========================================

def moeda(preco=0, moeda='R$'):
    """Formata um valor numérico para o padrão monetário."""
    return f'{moeda}{preco:>7.2f}'.replace('.', ',')


def aumentar(preco=0, taxa=0, formato=False):
    """Aumenta o preço e aceita formatação automática."""
    res = preco + (preco * taxa / 100)
    return res if not formato else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    """Diminui o preço e aceita formatação automática."""
    res = preco - (preco * taxa / 100)
    return res if not formato else moeda(res)


def dobro(preco=0, formato=False):
    """Dobra o preço e aceita formatação automática."""
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco=0, formato=False):
    """Divide o preço por dois e aceita formatação automática."""
    res = preco / 2
    return res if not formato else moeda(res)


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

p = float(input('Digite o preço: R$ '))

# O segundo (ou terceiro) parâmetro 'True' ativa a formatação automática
print(f'A metade de {moeda(p)} é {metade(p, True)}')
print(f'O dobro de {moeda(p)} é {dobro(p, True)}')
print(f'Aumentando 10%, temos {aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {diminuir(p, 13, True)}')
