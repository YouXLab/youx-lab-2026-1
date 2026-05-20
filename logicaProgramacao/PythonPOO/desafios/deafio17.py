from rich.table import Table
from rich import print

class Produto:
    def __init__(self, produto, preco):
        self.produto = produto
        self.preco = preco

    def etiqueta(self):
        etiqueta = Table(title='Produto')
        etiqueta.add_column(f'{self.produto}', justify='center')
        etiqueta.add_row(f'R${self.preco:,}')
        print(etiqueta)


produto1 = Produto('Iphone 17 Pro Max', 17000)
produto2 = Produto('Relógio', 370)
produto1.etiqueta()
produto2.etiqueta()