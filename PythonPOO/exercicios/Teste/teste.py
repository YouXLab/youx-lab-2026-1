#Declaraçao de classes
class Teste:
    def __init__(self): #metodo construtor
        self.nome = ''
        self.idade = 0

    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"O {self.nome} tem {self.idade} anos"

#Declaraçao de objetos
g1 = Teste()
g1.nome = 'Joao'
g1.idade = 17
g1.aniversario()
print(f"{g1.mensagem()}")