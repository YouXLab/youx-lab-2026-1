from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def etiqueta(self):
        conteudo = f'{self.nome.center(30, ' ')}'
        conteudo += f'{'-'*30}'
        precoform = f'R${self.preco:,.2f}'
        conteudo += f'\n{precoform.center(30, '-')}'
        etiqueta = Panel(conteudo, title='Produto', width=34)
        print(etiqueta)

p1 = Produto('AirFryer', 2700)
p2 = Produto('Logitech G Pro Superlight', 770)
p1.etiqueta()
p2.etiqueta()