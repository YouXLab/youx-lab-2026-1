from rich import print
from rich.panel import Panel

class churrasco:
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant
    def analisar(self):
        conteudo = f'Analisando {self.titulo} com {self.quant} convidados!'
        quantpessoa = self.quant * 0.4
        precocarne = quantpessoa * 82.40
        conteudo = f'Cada participante comerá 0.4Kg e a carne está R$82.40/kg'
        conteudo = f'Recomendo comprar {precocarne:.2f}Kg de carne'
#        precoform = f'R${self.preco:,.2f}'
#        conteudo += f'\n{precoform.center(30, '-')}'
        etiqueta = Panel(conteudo, title=f'{self.titulo}', width=34)
        print(etiqueta)

c1 = churrasco('Churras da Copa', 7)
c1.analisar()
# Consumo padrão: 400g p/ pessoa
# Preço: R$82,40/Kg