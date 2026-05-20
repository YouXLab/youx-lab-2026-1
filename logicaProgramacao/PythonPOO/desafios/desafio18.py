from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self, titulo, amigos):
        self.titulo = titulo
        self.amigos = amigos
        self.quantidade = 0.4 * amigos
        self.custo = self.quantidade * 82.40
        self.pessoa = self.custo / amigos

    def analisar(self):
        analise = Panel(f'''Analisando {self.titulo} com {self.amigos} pessoas
Cada participante comerá 0.4Kg de carne e cada Kg de carne custa R$82,40
Recomendo comprar {self.quantidade}Kg de carne
O custo total sera de R${self.custo:.2f} para participar
Cada pessoa pagará R${self.pessoa:.2f}''', title=self.titulo)
        print(analise)

churras = Churrasco('Saroba', 22)
churras.analisar()