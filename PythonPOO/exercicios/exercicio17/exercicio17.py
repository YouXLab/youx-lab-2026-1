class Produto:
    def __init__(self, nome = '', preco = 0):
       self.nome = nome
       self.preco = preco
    def etiqueta(self):
        return f'{self.nome} \n {self.preco}'

p1 = Produto('Iphone' ,15000 )
p1.etiqueta()


